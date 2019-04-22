import random

health = 50
print(health ,end = '')
difficulty = 2
potion_health = int(random.randint(25,50)/difficulty)

health = health + potion_health 

print(health)
