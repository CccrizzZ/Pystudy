class Man:
    gender = "male"

    def __init__(self, name):
        self.name = name


Chris = Man("Chris")

# String don't need a ()
print(Chris.name)
print(Chris.gender)
