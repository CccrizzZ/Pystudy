# Open a file in write mode
# If the file don't exist, this create the file for us
fw = open("./Python/sample.txt", "w")
# Writing Strings in the file
fw.write("This is sample.txt \n")
fw.write("I will drink until I pass out \n")
# Close the file
fw.close()

# Reading the file
fr = open("./Python/sample.txt", "r")
text = fr.read()
print(text)
# Close the file
fr.close()
