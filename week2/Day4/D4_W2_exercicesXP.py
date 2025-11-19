#Exercice 1
import random

def get_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return
def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    if not words:
        return "Impossible de générer une phrase sans mots."
    sentence = " ".join(random.choice(words) for _ in range(length))
    return sentence.lower()
def main():
    print("Ce programme génère une phrase aléatoire à partir d’un fichier de mots.")
    try:
        user_input = int(input("Entrez la longueur de la phrase (entre 2 et 20 mots) : "))
        if 2 <= user_input <= 20:
            sentence = get_random_sentence(user_input)
            print("Phrase générée :", sentence)
        else:
            print("Erreur : Veuillez entrer un nombre entre 2 et 20.")
    except ValueError:
        print("Erreur : Entrée invalide, veuillez entrer un nombre entier.")
if __name__ == "__main__":
        main()

#exercice2
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
#afficher le salaire
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)
# date de naissance
data["company"]["employee"]["birth_date"] = "27-11-1982"
with open("modified_company.json", "w") as file:
    json.dump(data, file, indent=4)
print("JSON modifié sauvegardé dans 'modified_company.json'")
