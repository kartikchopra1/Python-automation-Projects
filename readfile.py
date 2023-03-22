file = open("spider.txt")
print(file.readline())    # to read single line

print(file.read())           # read remaing lines

file.close()
with open("spider.txt") as file:
    print(file.readline())       # to close file

# print file in upper case

with open("spider.txt") as file
for line in file
print(line.upper())

# print file uppar case and withot spaces
with open("spider.txt") as file
for line in file
print(line.strip().upper())

# list and printing in sequence
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)
