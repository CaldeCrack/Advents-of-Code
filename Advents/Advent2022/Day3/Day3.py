# First Star
data = open("data.txt", "r")
newData = data.readlines()
rucksacks = [[rucksack.strip()[:(((len(rucksack)-2)//2)+1)], rucksack.strip()[(len(rucksack)//2):]] for rucksack in newData]
matches = [[item for item in compartments[0] if item in compartments[1]] for compartments in rucksacks]
priorities = [ord(item[0])-96 if ord(item[0])>96 else ord(item[0])-38 for item in matches]

#Second Star
rucksacks = [newData[x:x+3] for x in range(0, len(newData), 3)]
matches = [[item for item in compartments[0].strip() if (item in compartments[1].strip() and item in compartments[2].strip())] for compartments in rucksacks]
priorities2 = [ord(item[0])-96 if ord(item[0])>96 else ord(item[0])-38 for item in matches]
print("sum of first priorities:" , str(sum(priorities)) + ", sum of second priorities:" , str(sum(priorities2)))