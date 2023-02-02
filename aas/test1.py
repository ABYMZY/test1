f = open("test.txt", "w+")
f.write("1Now the file has more content!\n")
f.write("2Now the file has more content!\n")
f.write("3Now the file has more content!\n")
f.write("4Now the file has more content!\n")
f.write("5Now the file has more content!\n")
f.write("6Now the file has more content!\n")
f.write("7Now the file has more content!")

with open('test.txt', "r") as f:
    lines = [line.rstrip() for line in f]
[print(i) for i in lines]
# print(f.read())