class Enemy:
    life = 3

    # self same as this in JavaScript
    def attack(self):
        print("ouch!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()

enemy1.attack()
enemy1.check_life()
enemy1.attack()
enemy1.attack()
enemy1.check_life()


enemy2 = Enemy()

enemy2.attack()
enemy2.check_life()
