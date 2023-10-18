from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor, Item
from components import consumable
from components.inventory import Inventory
from components.level import Level

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Netrunner", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),    
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

guard = Actor(
    char="G", 
    color=(255, 255, 0), 
    name="Guard", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),   
    inventory=Inventory(capacity=0), 
    level=Level(xp_given=25),
)

shinobi = Actor(
    char="S",
    color=(255, 255, 0),
    name="Shinobi",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

nanogauze = Item(
    char="!",
    color=(127, 0, 255),
    name="Nanogauze",
    consumable=consumable.HealingConsumable(amount=4),
)

mathogen = Item(
    char="~",
    color=(255, 255, 0),
    name="Mathogen",
    consumable=consumable.MathogenConsumable(damage=20, max_range=5),
)

braindos = Item(
    char="~",
    color=(207, 63, 255),
    name="Braindos",
    consumable=consumable.ConfusionConsumable(number_of_turns=5),
)

empgrenade = Item(
    char="#",
    color=(255, 0, 0),
    name="EMP Grenade",
    consumable=consumable.EMPConsumable(damage=12, radius=3),
)