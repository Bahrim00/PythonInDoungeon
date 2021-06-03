class Player():
    def __init__(self, nume, mana, health, damage):
        self.nume = nume
        self.mana = mana
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Warrior(Player):
    def __init__(self, name, mana, health, damage):
        super.__init__(name, mana(0), health(10), damage(10))


class Wizard(Player):
    def __init__(self, name, mana, health, damage):
        super.__init__(name, mana(10), health(10), damage(0))