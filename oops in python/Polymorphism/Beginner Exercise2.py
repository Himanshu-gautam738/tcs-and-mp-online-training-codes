# Base class: Animal
class Animal:
    def makeSound(self):
        """Virtual method to be overridden by derived classes"""
        print("Some generic animal sound")


# Derived class: Dog
class Dog(Animal):
    def makeSound(self):
        print("Woof! Woof!")


# Derived class: Cat
class Cat(Animal):
    def makeSound(self):
        print("Meow! Meow!")


# Derived class: Cow
class Cow(Animal):
    def makeSound(self):
        print("Moo! Moo!")


# Demonstrate polymorphism
if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow()]  # List of Animal references

    for animal in animals:
        animal.makeSound()  # Correct overridden method is called at runtime
