# First Star
data = open("data.txt", "r") # no care about closing the file
newData, calories, n = data.readlines(), [], 0

for line in newData:
    if line == "\n" or line == "":
        calories.append(n)
        n = 0
        continue
    n += int(line[:-1])

# Second Star
calories.sort()
print("max:" , str(calories[-1]) + ", sum of the highest three:" , str(sum(calories[-3:])))
