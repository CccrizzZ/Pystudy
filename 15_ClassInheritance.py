class Parent():
    def print_last_name(self):
        print("L")

# Inheritance Parent()
class Child(Parent):
    def print_first_name(self):
        print("Chris")

    # Overwrite function in Parent()
    def print_last_name(self):
        print("Schaffhausen")

Chris = Child()

Chris.print_first_name()
Chris.print_last_name()
