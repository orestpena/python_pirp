# _*_ coding: utf-8 -*-
"""
this is a temp file on classes
"""

#class ClassName:
#
#     def __init__(self)
#         self.Attribute = 0
#
#     def AnotherFunction(self):
#         Action(s)

from argparse import Action


class Team:
    def __init__(self,Name = "Name",Origin = "Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def DefineTeamName(self, Name):
        self.TeamName = Name
    
    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin

#class InheritanceClassName(ParentClass):
#    def __init__(self, Input1, Input2):
#        ParentClass.__init__(self)
#        self.Attribute1 = Input1
#        self.Attribute2 = Input2
#        self.Attribute3 = 0
#
#    def AnotherMetod(self):
#        Action(s)

class Player(Team):
    #def __init__(self):
    def __init__(self,PlayerName, PPoints, TeamName, TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PPoints # the names do not have to be identical.

    def ScoredPoint(self):
        self.PlayerPoints += 1

    def setName(self,Name):
        self.PlayerName = Name

    def __str__(self):
        #return "Player has scored: " + str(self.PlayerPoints) + " Points"
        return self.PlayerName + " has scored: " + str(self.PlayerPoints) + " Points"

Player1 = Player("Sid",0,"Sharks","Chicago")

print(Player1.PlayerName)
print(Player1.PlayerPoints)
#Player1.DefineTeamName("Sharks")
print(Player1.TeamName)     # since we are accessing attributes or variables we do not need the open and close parentheses
print(Player1.TeamOrigin)

Player1.ScoredPoint()    # because we are accessing methods or funttions we need the open and close parentheses
print(Player1.PlayerPoints)

Player1.setName("Lee")

print(Player1.PlayerName)


print(Player1)