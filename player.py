import sys
import os


class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.pots = 0
        self.weapon = ["Rusty Sword"]
        self.current_weapon = ["Rusty Sword"]

    @property
