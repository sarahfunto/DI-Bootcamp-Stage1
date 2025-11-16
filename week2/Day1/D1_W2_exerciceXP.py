#exercice 1
class Cat :
    def __init__(self, cat_name,cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("chouquette", 8)
cat2 = Cat("Luna", 3)
cat3 = Cat("Simba", 5)

def find_oldest_cat(cat1, cat2, cat3):
    oldest = max([cat1, cat2, cat3], key=lambda cat: cat.age)
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} does woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

Mikas_dog = Dog("Rex", 50)
sarahs_dog = Dog("Brutus", 20)
for dog in [Mikas_dog, sarahs_dog]:
    print(f"{dog.name} is {dog.height} cm tall.")
    dog.bark()
    dog.jump()
if Mikas_dog.height > sarahs_dog.height:
    print(f"{Mikas_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")

#Exercice 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
stairway.sing_me_a_song()

#Exercice 4
class Zoo :
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
    def get_animals(self):
        print("Animals in the zoo:", self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        self.groups = {}
        for animal in self.animals:
            letter = animal[0].upper()
            if letter not in self.groups:
                self.groups[letter] = []
            self.groups[letter].append(animal)
    def get_groups(self):
        for key in self.groups:
            print(f"{key}: {self.groups[key]}")
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Cougar", "Cat", "Zebra", "Lion")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()