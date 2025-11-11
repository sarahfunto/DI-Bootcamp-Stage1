# Exercise 1
number_info = ["ten", "twenty", "thirty"]
number = {"ten" :10,
          "twenty" : 20,
          "thirty" : 30}
print(number)

# Exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
print(family)
total_cost = 0
for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{member.capitalize()} pays {price} dollars")    

    total_cost += price
print(f"Total cost for the family is {total_cost} dollars") 

# Exercise 3
brand = {
  "name": "Zara",
  "creation_date": 1975,
  "creator_name": "Amancio Ortega Gaona",
  "type_of_clothes": ["men", "women", "children", "home"],
  "international_competitors": ["Gap", "H&M", "Benetton"],      
  "number_stores": 7000,
  "major_color":{
    "France": "blue", 
    "Spain": "red", 
"US": ["pink", "green"]
  }
}
print(brand)
brand["number_stores"] = 2
print(brand["number_stores"])
print(f"Zara's clients are: {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"]="Spain"
print(brand)
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"][-1])
del brand["creation_date"]
print(brand)    
print(brand["major_color"]["US"])
print("Number of keys in brand:", len(brand))
print("All keys in brand:", list(brand.keys()))

# Exercise 4
Disney_characters = {
    "Mickey": 0, 
    "Minnie": 1,   
    "Donald": 2, 
    "Ariel": 3, 
    "Pluto": 4 
    }
print(Disney_characters)
Disney_characters_inv = {
    0 : "Mickey", 
    1 : "Minnie",   
    2 : "Donald", 
    3 : "Ariel", 
    4 : "Pluto" 
    }
print(Disney_characters_inv)
Disney_characters_opp = {
    "Ariel" : 0, 
    "Donald" : 1,   
    "Mickey" : 2, 
    "Minnie" : 3, 
    "Pluto" : 4
    }
print(Disney_characters_opp)
