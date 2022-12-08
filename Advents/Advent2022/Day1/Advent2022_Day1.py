# First Star
data = open("C:/Users/ninja/OneDrive/Escritorio/Cosas de la U/Otros/Scripts/Advent2022/Day1/data.txt", "r")
newData = data.readlines()
calories = []

n = 0
for line in newData:
    if line == "\n" or line == "":
        calories.append(n)
        n = 0
        continue
    n += int(line[:-1])

print(max(calories))

# Second Star
calories.sort()
print(calories[-3]+calories[-2]+calories[-1])