# For Loop
foods = ["taco", "taco","taco","beer"]
for i in foods:
    print(i)
    print(len(i))



# While Loop
x = 90
while x < 100:
    print(x)
    x+=1  # Increment



# Range
for i in range(10):  # Outputs 0~9
    print(i)

for i in range(10,40,2): # range(starts,ends,increment) excludes end
    print(i)

for i in range(len(foods),-1,-1):
    print(i)

for i in range(10):
    print("*"*i)



# All prime numbers from 2 to 100
for i in range(2,100+1):
    if i > 1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            print(i)
