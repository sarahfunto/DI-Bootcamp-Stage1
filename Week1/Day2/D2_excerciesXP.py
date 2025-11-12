my_fav_numbers = {3, 7, 10, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(12)
my_fav_numbers.remove(12)
print(my_fav_numbers)

friend_fav_numbers = {5, 9, 15}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)  

#excercie 2
my_tuple = (1, 2, 3)
print(my_tuple)
new_tuple = my_tuple + (4, 5)
print(new_tuple)

#excercie 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
apples_count = basket.count("Apples")
print("Number of Apples:", apples_count)
basket.clear()
print(basket)

#excercie 4
list = [x * 0.5 for x in range(3, 11)]
print(list)

#excercie 5
for number in range(1, 21):
    print(number)
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
print("--------")
#excercie 6
while True:
    name = input("Enter your name: ")
    if not name.isdigit() and len(name) >= 3:
        print("Thank you!")
        break
    else:
        print("Invalid name. Please enter at least 3 letters and no digits.")

#excercie 7
favorite_fruits = input("Enter your favorite fruits (separated by spaces): ").split()
fruit = input("Enter the name of a fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")  
else:   
    print("You chose a new fruit. I hope you enjoy it!")

#excercie 8
toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = 10 + 2.5 * len(toppings)
print("\nToppings:", ", ".join(toppings))
print(f"Total price: ${total_price:.2f}")

#excercie 9
total_cost = 0
family_size = int(input("How many people want to buy a ticket? "))

for i in range(family_size):
    age = int(input(f"Enter the age of person #{i + 1}: "))
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost

print(f"\nTotal ticket cost: ${total_cost}")
