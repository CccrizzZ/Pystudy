class Tuna(object):
    def __init__(self):
        print("Init function called")

    def swim(self):
        print("Swimming")

# __init__ function is called when new variable is created under this class
tuna = Tuna()
tuna.swim()




class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jsn = Enemy(10)
jsn.get_energy()

jke = Enemy(8)
jke.get_energy()
