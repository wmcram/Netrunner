from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),    
)

guard = Actor(
    char="G", 
    color=(255, 255, 0), 
    name="Guard", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),    
)

shinobi = Actor(
    char="S",
    color=(255, 255, 0),
    name="Shinobi",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)