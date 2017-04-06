import sys
import os


class Player():
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 100
        self.pots = 0
        self.weapon_inventory = ["Rusty Sword"]
        self.current_weapon = ["Rusty Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.current_weapon == "Rusty Sword":
            attack +=5
        if self.current_weapon == "Great Sword":
            attack+=15
        return attack

