# --- Day 3: Rucksack Reorganization ---
# https://adventofcode.com/2022/day/3


def priorityMap(item: str) -> int:
	return ord(item[0]) - 96 if ord(item[0]) > 96 else ord(item[0]) - 38


rucksacks: list[str] = []
while content := input():
	rucksacks.append(content)

divided_rucksacks: list[list[str]] = [
	[content[:len(content) // 2], content[len(content) // 2:]] for content in rucksacks
]
matches: list[str] = []
for compartments in divided_rucksacks:
	for item in compartments[0]:
		if item in compartments[1]:
			matches.append(item)
			break
total_priority = sum(map(priorityMap, matches))

badges: list[str] = []
for i in range(0, len(rucksacks), 3):
	for item in rucksacks[i]:
		if item in rucksacks[i + 1] and item in rucksacks[i + 2]:
			badges.append(item)
			break
total_badge_priority = sum(map(priorityMap, badges))

print(f'Part 1 solution: {total_priority}')
print(f'Part 2 solution: {total_badge_priority}')
