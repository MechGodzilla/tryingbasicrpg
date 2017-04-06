# A better approach to this and the video's method is inheritance, create an Enemy() class as you said above and then have other classes such as
# Goblin(Enemy) inherit from the Enemy(object) with the super().__init__() method.﻿
# https://stackoverflow.com/questions/23117717/python-super-init-inheritance
# from player import Player
#
#
# class Goblin(Player):
#     def __init__(self, name):
#         super(Goblin, self).__init__(name)
#         self.maxhealth = 50
#         self.health = self.maxhealth
#         self.attack = 5
#         self.goldGain = 10
#
#
# class Zombie(Player):
#     def __init__(self, name):
#         super(Zombie, self).__init__(name)
#         self.maxhealth = 70
#         self.health = self.maxhealth
#         self.attack = 7
#         self.goldGain = 15
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldGain = 10


class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldGain = 15