from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor, Item
from components import consumable, equippable
from components.inventory import Inventory
from components.level import Level
from components.equipment import Equipment

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Netrunner", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, base_defense=2, base_power=4),    
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
    equipment=Equipment(),
)

guard = Actor(
    char="G", 
    color=(255, 255, 0), 
    name="Guard", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, base_defense=0, base_power=3),   
    inventory=Inventory(capacity=0), 
    level=Level(xp_given=25),
    equipment=Equipment(),
)

shinobi = Actor(
    char="S",
    color=(255, 255, 0),
    name="Shinobi",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
    equipment=Equipment(),
)

boss = Actor(
    char="@",
    color=(255, 255, 50),
    name="Netrunner",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=100, base_defense=4, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=99999),
    equipment=Equipment(),
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

bitshiv = Item(
    char="/",
    color=(255, 255, 255),
    name="Bitshiv",
    equippable=equippable.Bitshiv(),
)

automakatana = Item(
    char="/",
    color=(255, 255, 255),
    name="Automakatana",
    equippable=equippable.Automakatana(),
)

slipsuit = Item(
    char="[",
    color=(0, 255, 0),
    name="Slipsuit",
    equippable=equippable.Slipsuit(),
)

datamail = Item(
    char="[",
    color=(0, 255, 0),
    name="Datamail",
    equippable=equippable.Datamail(),
)