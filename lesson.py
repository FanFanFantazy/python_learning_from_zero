class battle:
    hp = 0
    cp = 0
    weappon = 99

    def __init__(self, hp, cp):
        self.hp = hp
        self.cp = cp
        print(self.hp)
        print(self.cp)

    def attack(self):
        print(self.weappon)


class archer(battle):
    arrow = 0

    def __init__(self, hp, cp):
        battle.__init__(self, hp, cp)

    def attack(self, arrow):
        self.arrow = arrow - 1
        print(self.arrow)


archer(100, 100).attack(20)
