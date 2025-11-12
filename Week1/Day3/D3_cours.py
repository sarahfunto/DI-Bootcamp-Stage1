student_info = ["HArry", "Potter", 15, "Private Drive 4" , "Hedwig", "buckbeak"]
student_info = { "first_name": "Harry",
                 "last_name": "Potter",
                 "age": 15,
                "address": "Private Drive 4",
                "pets": ["Hedwig", "buckbeak"],
                "best_friend": ("Ron Weasley", "Hermione Granger"),
                "is parselmouth" : True, 
                "house": {"main" : "Gryffindor", "seconde": "Slytherin"}}

print(student_info ["first_name"])
print(student_info["pets"])
student_info ["pets"].append ("toby") 
student_info["pets"][1]
print(student_info)
print(student_info["house"]["main"])
print(student_info["first_name"].upper())

student_info[0] = "Tiago"  # This will raise an error because student_info is a dictionary, not a list.
student_info["first_name"] = "Tiago"  # Correct way to change the first name in the dictionary
print(student_info)

#EXERCICES
#1. print Harry Potter's age
print(student_info["age"])
#2. add 10 years to his age and print again
student_info["age"] += 10
print(student_info["age"])
#3. change the adress to "betzalel 8"
student_info["address"] = "betzalel 8"
print(student_info["address"])  
#4. add a new pet "Crookshanks"
student_info["pets"].append("Crookshanks")  
print(student_info["pets"])
#5. change the Is_parselmouth to False
student_info["is parselmouth"] = False
print(student_info["is parselmouth"])
print(student_info)

#how to add a new key value pair
student_info["teachers"] = "Snap"
print(student_info)
student_info.update({"principal": "Dumbledore"})
print(student_info)
#how to delete a key value pair
del student_info["address"] 
print(student_info)

#looping through a dictionary
for item in student_info:
    print(item)

#options of looping through a dictionary
for key in student_info.keys():
    print(key)
for value in student_info.values():
    print(value)
    print(type(value))
for key, value in student_info.items():
    print(key, value)

#we want to change all the string values to uppercase
for value in student_info.values():
    if type(value) == str:
        student_info[key] = value.upper()
            
            
print(student_info)


    

#exercise 
sample_dict = { "class", "student", "name", "marks", "physics", "history"}
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict["class"]["student"]["marks"]["history"])  #output 80


