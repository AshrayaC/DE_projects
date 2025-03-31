# Defining a class named Character
class Character: 
    def __init__(self, health, damage, speed):
        # Initializing attributes when an object is created
        self.health = health   # Stores the character's health
        self.damage = damage   # Stores the character's attack damage
        self.speed = speed     # Stores the character's movement speed
    

# Creating an instance of Character representing a warrior
warrior = Character(100, 20, 10)  # Warrior has 100 health, 20 damage, 10 speed

# Creating another instance representing a ninja
ninja = Character(200, 100, 10)  # Ninja has 200 health, 100 damage, 10 speed

# Printing the speed attribute of the warrior
print(f"Warrior speed: {warrior.speed}")  # Output: Warrior speed: 10