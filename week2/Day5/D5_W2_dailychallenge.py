# excercie 1
# Answer the following questions:

#     What is a class? a blueprint
#     What is an instance? a real object
#     What is encapsulation? limit of attribute
#     What is abstraction? simplify the object
#     What is inheritance? created relation with an other class
#     What is multiple inheritance? created relation in several classes
#     What is polymorphism? using a class differently for different objects
#     What is method resolution order or MRO? organisation of classes.. :/

#exercice 2
import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []     # liste des cartes
        self.shuffle()      # mélanger les cartes 

    def shuffle(self):      # créer un jeu de 52 cartes et le melanger 
        self.cards = [Card(suit, value) 
                      for suit in Card.suits 
                      for value in Card.values]
        random.shuffle(self.cards)

    def deal(self):    #tirer une carte aleatoire
        if len(self.cards) == 0:
            return None  
        return self.cards.pop()  



deck = Deck()
print("Initial deck size:", len(deck.cards))

card = deck.deal()
print("Card dealt:", card)

print("Remaining cards:", len(deck.cards))

