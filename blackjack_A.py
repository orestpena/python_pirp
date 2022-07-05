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

#shuffle(cardDeck)

print(cardDeck)
