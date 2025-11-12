#exercise 1 

def display_message() :
    print(display_message)
    print("I am learning about functions in Python.")
display_message()

#exercise 2
def favorite_book(title):   
    print(f"One of my favorite books is {title}.")  
favorite_book("Alice in Wonderland")    

#exercise 3
def describe_city(city, country = "Iceland"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik")

describe_city("Paris", "unknwon")

#exercise 4
import random
def random_number(user_num):
    computer_num = random.randint(1, 100)
    if user_num == computer_num:
        print('Success!')
    else:
        print(f'{computer_num}, Fail')
    return computer_num
print(random_number(user_num=55))

#exercise 5
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.") 
make_shirt("L", "I love python")
make_shirt(text="I love python", size="M")
make_shirt(size="S", text="custom message")

#exercise 6
magicians_name = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_magicians(magician_names):
    for name in magician_names:
        print(name)
show_magicians(magicians_name)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = "The Great " + magician_names[i]
    return magician_names
great_magicians = make_great(magicians_name[:])
show_magicians(great_magicians) 

#exercise 7
import random
def get_random_temp():
    temp = random.randint(-10, 40)
    print(f"The temperature right now is {temp} degrees Celsius.")
    return temp
def main():
    temp = get_random_temp()
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("It's a bit warm today.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

main()

def get_random_temp(month):
    if month in [12, 1, 2]:  # hiver
        return round(random.uniform(-10, 10), 1)
    elif month in [3, 4, 5]:  # printemps
        return round(random.uniform(10, 20), 1)
    elif month in [6, 7, 8]:  # été
        return round(random.uniform(20, 40), 1)
    elif month in [9, 10, 11]:  # automne
        return round(random.uniform(10, 25), 1)
    else:
        return None
    
def main():
    month = int(input("Enter the month as a number (1-12): "))
    temp = get_random_temp(month)
    if temp is None:
        print("Invalid month. Please enter a number between 1 and 12.")
        return
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temp <= 23:
        print("It's a bit warm today.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")    
main()


        

