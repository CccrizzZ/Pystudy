# Print stuff
print(1+62)
print("awsdfawe")
print(abs(-99))


# Slice stuff
user = "Chris"
print(user[0])
print(user[1:5])


# Length function
print(len("Chris"))


# List
a = [1,2,3,4,5]
print(a[2])

a += [1,2,3,4]
print(a)

a.append(999)
print(a)

print(a[:4]) # End at 3 include 3

print(a[4:]) # Start from 4

print(a[2:6]) # Start from 2 end at 5 include 5

a[:] = [] # Empty all elements
print(a)
