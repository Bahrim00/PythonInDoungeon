class Enemy:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(5, 100)
        print('Glglgl!!! I am a Goblin and I will slash you!!! ')


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(15, 100)
        print('Wraar, I am a Orc and I will cut you down!!! ')


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(10, 100)
        print('Squil!! I am a Rat and I will eat you alivee!!! ')

