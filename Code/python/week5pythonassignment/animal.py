# Base Animal class
class Animal:
    # Constructor to set up the animal
    def __init__(self, name):
        self.name = name  # Animal name

    # Move method to be overridden
    def move(self):
        return f"{self.name} is moving"

# Dog subclass
class Dog(Animal):
    # Override move method
    def move(self):
        return f"{self.name} is running on land 🐶"

# Bird subclass
class Bird(Animal):
    # Override move method
    def move(self):
        return f"{self.name} is flying in the sky 🐦"

# Fish subclass
class Fish(Animal):
    # Override move method
    def move(self):
        return f"{self.name} is swimming in water 🐠"

# Test the classes
def main():
    # Create animals
    dog = Dog("Rex")
    bird = Bird("Tweety")
    fish = Fish("Nemo")

    # List of animals
    animals = [dog, bird, fish]

    # Show how each animal moves
    print("Animal Movements:")
    for animal in animals:
        print(animal.move())

if __name__ == "__main__":
    main()