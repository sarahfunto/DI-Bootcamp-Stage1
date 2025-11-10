#Exercice 1
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)


#Exercice 2
word = input("Enter a word: ")
new_word = word[0]
for char in word[1:]:
    if char != new_word[-1]:
        new_word += char

print(new_word)
