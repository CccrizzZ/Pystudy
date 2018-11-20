# Functions in Python
def usd_to_cad(usd):
    return usd * 1.25

# Printing variables and strings
print usd_to_cad(5),"CAD"

a = usd_to_cad(9)

print a,"CAD"


# Default value for functions
def get_gender(sex="Unknown"):
    if sex is 1:
        sex="Male"
    if sex is 0:
        sex="Female"
    return sex

gender1 = 1
gender2 = 0

print(get_gender(gender1))
print(get_gender(gender2))
print(get_gender())



# Key words arguments
def sentence(name="Chirs", action="Eating", place="Mars"):
    return str(name)+" "+str(action)+" "+str(place)

print sentence()
print sentence("Dave","Dive","Deep")
print sentence(name="Mark")



# Flexible number of arguments
def add_arg(*args):
    total_arg = 0
    # Traverse all arguments and add them to total_arg
    for i in args:
        total_arg += i
    return total_arg

print add_arg(4,5,6,7,8,9)





# Unpacking arguments
def health_calc(age, apples_ate, cig_smoked):
    return (100-age) + (apples_ate*3.5) - (cig_smoked*2)

Chris_data = [20, 5, 10]

# Using *Array
print(health_calc(Chris_data[0], Chris_data[1], Chris_data[2]))
print(health_calc(*Chris_data))
