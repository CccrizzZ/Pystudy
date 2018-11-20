class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def eat_shroom(self):
        print("Now I am big")

# Multiple inheritance
# This class can call all function in classes above⬆️
class BigMario(Mario, Shroom):
    # Do nothing and handles the syntax error
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
