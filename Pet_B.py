#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Pet class
adding Dog class
"""

from unicodedata import name


class Pet:
    def __init__(self,name,a,h,p):
        self.name = name
        self.age = a
        self.hunger = h
        self.playful = p

    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

    #setters
    def setName(self,xname):
        self.name = xname

    def setAge(self,Age):
        self.age = Age

    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayful(self,play):
        self.playful = play

class Dog(Pet):
    def __init__(self, name, age, hunger, playful, breed, FavoriteToy):
        Pet.__init__(self,name,age,hunger,playful)
        self.breed = breed
        self.FavoriteToy = FavoriteToy

    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.FavoriteToy)
        else:
            return ("Dog doesn't want to play")

huskyDog = Dog("Snowball",5,False,True,"Husky","Stick")

Play = huskyDog.wantsToPlay()

print(Play)

huskyDog.playful = False

Play = huskyDog.wantsToPlay()

print(Play)