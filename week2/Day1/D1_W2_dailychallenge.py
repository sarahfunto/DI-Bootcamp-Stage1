class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {} 
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    def get_info(self):
        output = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            output += f"{animal:<10} : {count}\n"
        output += "\nE-I-E-I-0!"
        return output

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 1)
macdonald.add_animal("sheep", 2)
macdonald.add_animal("cow", 3)
macdonald.add_animal("pig", 5)

print(macdonald.get_info())