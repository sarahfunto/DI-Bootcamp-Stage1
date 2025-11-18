#Exercice 1 

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.str()

    def __int__(self):
        return self.amount
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, (int, float)):
            return self.amount + other
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, (int, float)):
            self.amount += other
        else:
            raise TypeError("Unsupported operand type(s) for +=")
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)

# #Exercice 2
# #def add_numbers(a, b):
#     result = a + b
#     print(f"La somme est : {result}")
# # from func import add_numbers
# add_numbers(4, 7)

#Exercice 3

import string
import random

all_letters = string.ascii_letters  # contient a-z + A-Z
random_string = ''.join(random.choice(all_letters) for _ in range(5))

print(random_string)

#Exercice 4
import datetime  

def display_current_date():
    today = datetime.date.today() 
    formatted_date = today.strftime("%d/%m/%Y")  
    print("Date actuelle :", today)
    print ("Date actuelle format fr :", formatted_date)  

display_current_date()

#Exercice 5
import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    next_jan1 = datetime.datetime(year=now.year + 1, month=1, day=1)
    time_left = next_jan1 - now
    print("Temps restant jusqu'au 1er janvier :", time_left)

time_until_new_year()

#Exercice 6
from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    now = datetime.now()
    time_lived = now - birthdate
    minutes = int(time_lived.total_seconds() // 60)

    print(f"Vous avez vécu environ {minutes} minutes.")
minutes_lived("27-11-1982")

#Exercice 7
from faker import Faker
faker = Faker()
users = []
def generate_users(n):
    for _ in range(n):
        user = {
            'name': faker.name(),
            'address': faker.address(),
            'language_code': faker.language_code()
        }
        users.append(user)
generate_users(5)

for user in users:
    print(user)