# --- Day 1: Historian Hysteria ---
# https://adventofcode.com/2024/day/1

idList1: list[int] = []
idList2: list[int] = []
frequencies: dict[int, int] = {}
while ids := list(map(int, input().split())):
	idList1.append(ids[0])
	idList2.append(ids[1])
	frequencies[ids[1]] = frequencies.get(ids[1], 0) + 1

idList1.sort()
idList2.sort()

distance: int = 0
similarity: int = 0
for i, value in enumerate(idList1):
	distance += abs(value - idList2[i])
	similarity += value * frequencies.get(value, 0)

print(f'Part 1 solution: {distance}')
print(f'Part 2 solution: {similarity}')
