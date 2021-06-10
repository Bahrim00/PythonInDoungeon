class Player():
    def __init__(self, nume, mana, health, damage):
        self.nume = nume
        self.mana = mana
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 0, 100, 50)


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 50, 100, 0)