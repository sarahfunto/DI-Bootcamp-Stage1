menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu):
    print("Current menu:")
    for drink, price in menu.items():
        print(f"{drink} - {price}₪")

def add_item(menu):
    drink = input("Enter new drink name: ").lower()
    if drink in menu:
        print("Item already exists!")
    else:
        price = float(input("Enter price: "))
        menu[drink] = price
        print(f'"{drink}" added!')

def update_price(menu):
    drink = input("Which drink do you want to update? ").lower()
    if drink in menu:
        new_price = float(input("Enter the new price: "))
        menu[drink] = new_price
        print("Price updated!")
    else:
        print("Item not found.")

def delete_item(menu):
    drink = input("Which drink do you want to delete? ").lower()
    if drink in menu:
        del menu[drink]
        print("Item deleted!")
    else:
        print("Item not found.")

while True:
    print("\nWhat would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")
    choice = input("> ")    
    if choice == "1":
        show_menu(menu)
    elif choice == "2":
        add_item(menu)
    elif choice == "3":
        update_price(menu)
    elif choice == "4":
        delete_item(menu)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")  
