from random import uniform

file = open("data.txt", "w")

for _ in range(20):
    file.write(str(uniform(0, 10)) + " " + str(uniform(0, 10)) + "\n")

file.close()
