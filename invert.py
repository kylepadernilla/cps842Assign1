f = open("test.txt","r")
lines = f.readlines()
for i in lines:
    thisline = i.split(" ")

print(lines)
