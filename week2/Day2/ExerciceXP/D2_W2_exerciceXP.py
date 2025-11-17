#Exercice 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking gracefully.")

cat1 = Siamese("chouquette")
cat2 = Siamese("Luna")
cat3 = Siamese("Oliver")

all_cats = [cat1, cat2, cat3]

class Pets:
    def _init_(self, cats):
        self.cats = cats

    def walk(self):
        for cat in self.cats:
            cat.walk()

    sara_pets = Pets(all_cats)
    sara_pets.walk()

#Exercice 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"
        else:
            return "It/’s a draw!"
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Bob", 3, 18)
dog3 = Dog("Max", 6, 25)
    
print(dog1.bark())
print(f"{dog2.name}'s speed: {dog2.run_speed():.2f}")
print(dog1.fight(dog2))

#Exercice 3
from dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
    def play(self, *dogs):
        dog_names = [self.name] + list(dogs)
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Bob", "Max")
my_dog.do_a_trick()            

#Exercice 4
class Person:
    def _init_(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
    
class Family:
    def _init_(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, age {member.age}")
        smith_family = Family("Smith")
        smith_family.born("Rivka", 17)
        smith_family.born("Adam", 20)

        smith_family.family_presentation()
        smith_family.check_majority("Rivka")
        smith_family.check_majority("Adam")