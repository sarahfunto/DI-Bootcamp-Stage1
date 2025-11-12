#fonctions


#syntac of a fonction : WARNING impotant de 'appeler la fonction

def greeting():
    print("Welcome, user!")

greeting()  #appel de la fonction

def greeting(user_name):
    print("Welcome, " + user_name + "!")

greeting("Alice")  #appel de la fonction avec un argument
greeting("Bob")    #appel de la fonction avec un autre argument
def greeting(user_name, language):
    if language == "EN":
        print("Welcome, " + user_name + "!")
    elif language == "PT":
        print("Bem-vindo, " + user_name + "!")
    elif language == "IT":
        print("Benvenuto, " + user_name + "!")
    elif language == "RU":
        print("Privet, " + user_name + "!")
    else:
        print("Welcome, " + user_name + "!") #default to English

greeting("Alice", "EN")  #appel de la fonction avec deux arguments
greeting("Bruno", "PT")  #appel de la fonction avec deux arguments
greeting("Carla", "IT")  #appel de la fonction avec deux arguments
greeting("Dmitri", "RU")  #appel de la fonction avec deux arguments
greeting("Eve", "FR")    #appel de la fonction avec deux arguments, default case
# les arguments peuvent avoir des valeurs par défaut
#WARNING the keyword argument must be placed after the positional arguments

#exercice
def country_info(country):
    if country == "USA" :
        print ("Washington")      
    
    
country_info ("USA")
    elif country == "France" :
        print ("Paris")
    elif country == "Italy" :
        print ("Rome")
    elif country == "Germany" :
        print ("Berlin")
    elif country == "Naboo" :
        print ("theed")
    else :
        print ("Country not found")

#RANDOM
import random   

def compare_random(user_number):
    computer_number = random.randint(1, 100)  #génère un nombre aléatoire entre 1 et 10
    if user_numbernumber == computer_number:
        print("Success! ")
    else:
        print(f'{computer_number}, Fail")
compare_random(50)  #appel de la fonction avec un argument


def get_random_temperature():
    return random.randint(-10, 35)  #génère un nombre aléatoire entre -10 et 35
    current_temperature = get_random_temperature()
#appel de la fonction et stockage de la valeur de retour    
    print(f'The current temperature is {current_temperature}°C')
    return current_temperature
current_temperature = get_random_temperature()


#SCOPEQ : GLOBAL AND LOCAL VARIABLES

fav_movie = "intersellar"  #variable globale

def movie_recomendation(fa_movie):
    recomend = "lost in Mars"  #variable locale
    return recomend

print(movie_recomendation(fav_movie))

#global variabl can be consulter into a scope local but not changed


    