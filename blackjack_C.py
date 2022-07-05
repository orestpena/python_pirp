#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#Creating a blackjack game
#either against a user or computer

from random import shuffle

def createDeck():
    Deck = []
    
    faceValues = ["A","J","Q","K"]
    for i in range(4):   #There are 4 different suits
        for card in range (2,11):   #Adding numbers 2,10
            Deck.append(str(card))

        for card in faceValues:
            Deck.append(card)
    
    shuffle(Deck)
    return Deck

cardDeck = createDeck()

#shuffle(cardDeck)   #moving the shuffle to inside the faceValues method

print(cardDeck)

class Player:

    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money

    def __str__(self): #allows us to call print on player  print(Player)
        currentHand = " "
        for card in self.hand:
            currentHand += str(card) + " "

        finalStatus = currentHand + "score: " + str(self.score)
        #"A 10 score: 21"
        return finalStatus

    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":11, "J":10, "Q":10, "K":10,
                         "2":2,"3":3,"4":4,"5":5,"6":6,
                         "7":7,"8":8,"9":9,"10":10}
        aceCounter = 0
        for card in self.hand:
                self.score += faceCardsDict[card]
                if card == "A":
                    aceCounter += 1
                if self.score > 21 and aceCounter != 0:
                    self.score -= 10
                    aceCounter -= 1
        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()

    def pay(self,amount):
        self.money -= amount
    
    def win(self,amount):
        self.money += amount

Player1 = Player(["3","7","5"])
print(Player1)
#Player1.hit("K")
Player1.hit("A")
Player1.hit("A")
print(Player1)
Player1.pay(20)
print(Player1.money)
Player1.win(40)
print(Player1.money)
Player1.play(["A","K"])
print(Player1)
print(Player1.money)
