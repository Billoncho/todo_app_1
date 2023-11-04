# Coding Exercise 4
# Use Python to create a file with name file.txt and write the text snail there.
import fileinput

content = "snail"

filename = open(f"XFiles/file.txt", 'w')
filename.write(content)
filename.close()