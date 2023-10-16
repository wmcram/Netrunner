from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import actions
import color
from components.base_component import BaseComponent
import components.inventory
import components.ai
from input_handlers import SingleRangedAttackHandler, AreaRangedAttackHandler
from exceptions import Impossible

if TYPE_CHECKING:
    from entity import Actor, Item
    
class Consumable(BaseComponent):
    parent: Item
    
    def get_action(self, consumer: Actor) -> Optional[actions.Action]:
        return actions.ItemAction(consumer, self.parent)
    
    def activate(self, action: actions.ItemAction) -> None:
        raise NotImplementedError()    
    
    def consume(self) -> None:
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)
    
class HealingConsumable(Consumable):
    def __init__(self, amount: int):
        self.amount = amount
        
    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)
        
        if amount_recovered > 0:
            self.engine.message_log.add_message(f"You inject the {self.parent.name}, and recover {amount_recovered} HP!", color.health_recovered)
            self.consume()
        else:
            raise Impossible(f"Your health is already full.")
        
        
class MathogenConsumable(Consumable):
    def __init__(self, damage: int, max_range: int):
        self.damage = damage
        self.max_range = max_range
        
    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        target = None
        closest_distance = self.max_range + 1.0
        
        #Find closest actor
        for actor in self.engine.game_map.actors:
            if actor is not consumer and self.parent.gamemap.visible[actor.x, actor.y]:
                distance = consumer.distance(actor.x, actor.y)
                
                if distance < closest_distance:
                    target = actor
                    closest_distance = distance
                    
        if target:
            self.engine.message_log.add_message(f"The Mathogen finds a vulnerability in {target.name} and deals {self.damage} damage!")
            target.fighter.take_damage(self.damage)
            self.consume()
        else:
            raise Impossible("There are no enemies close enough to target.")

class ConfusionConsumable(Consumable):
    def __init__(self, number_of_turns: int):
        self.number_of_turns = number_of_turns
        
    def get_action(self, consumer: Actor) -> Optional[actions.Action]:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        self.engine.event_handler = SingleRangedAttackHandler(
            self.engine,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy),
        )
        return None

    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        target = action.target_actor

        if not self.engine.game_map.visible[action.target_xy]:
            raise Impossible("You cannot target an area that you cannot see.")
        if not target:
            raise Impossible("You must select an enemy to target.")
        if target is consumer:
            raise Impossible("You probably shouldn't do that.")

        self.engine.message_log.add_message(
            f"The eyes of the {target.name} look vacant, as it starts to stumble around!",
            color.status_effect_applied,
        )
        target.ai = components.ai.ConfusedEnemy(
            entity=target, previous_ai=target.ai, turns_remaining=self.number_of_turns,
        )
        self.consume()

class EMPConsumable(Consumable):
    def __init__(self, damage: int, radius: int):
        self.damage = damage
        self.radius = radius

    def get_action(self, consumer: Actor) -> Optional[actions.Action]:
        self.engine.message_log.add_message(
            "Select a target location.", color.needs_target
        )
        self.engine.event_handler = AreaRangedAttackHandler(
            self.engine,
            radius=self.radius,
            callback=lambda xy: actions.ItemAction(consumer, self.parent, xy),
        )
        return None

    def activate(self, action: actions.ItemAction) -> None:
        target_xy = action.target_xy

        if not self.engine.game_map.visible[target_xy]:
            raise Impossible("You cannot target an area that you cannot see.")

        targets_hit = False
        for actor in self.engine.game_map.actors:
            if actor.distance(*target_xy) <= self.radius:
                self.engine.message_log.add_message(
                    f"The {actor.name} is shaken by the blast for {self.damage} damage!"
                )
                actor.fighter.take_damage(self.damage)
                targets_hit = True

        if not targets_hit:
            raise Impossible("There are no targets in the radius.")
        self.consume()