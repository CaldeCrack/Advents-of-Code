# --- Day 8: Resonant Collinearity ---
# https://adventofcode.com/2024/day/8
from collections import defaultdict


class coords:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def __add__(self, other):
		return coords(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return coords(self.x - other.x, self.y - other.y)

	def __hash__(self) -> int:
		return hash((self.x, self.y))

	def __eq__(self, other) -> bool:
		return self.x == other.x and self.y == other.y


antenna_coords: defaultdict[str, list[coords]] = defaultdict(list)
rows: int = 0
cols: int = 0
while row := input():
	for x, char in enumerate(row):
		if char.isalnum():
			antenna_coords[char].append(coords(x, cols))
	rows = len(row)
	cols += 1


def inBounds(point: coords) -> bool:
	return 0 <= point.x < rows and 0 <= point.y < cols


unique_pos: set[coords] = set()
unique_pos_2: set[coords] = set()
for key, values in antenna_coords.items():
	for i in range(len(values)):
		for j in range(i + 1, len(values)):
			first_pos: coords = values[i]
			second_pos: coords = values[j]
			distance: coords = second_pos - first_pos
			first_antinode: coords = second_pos + distance
			second_antinode: coords = first_pos - distance
			if inBounds(first_antinode):
				unique_pos.add(first_antinode)
			if inBounds(second_antinode):
				unique_pos.add(second_antinode)

			while inBounds(second_pos):
				unique_pos_2.add(second_pos)
				second_pos += distance
			while inBounds(first_pos):
				unique_pos_2.add(first_pos)
				first_pos -= distance

print(f'Part 1 solution: {len(unique_pos)}')
print(f'Part 2 solution: {len(unique_pos_2)}')
