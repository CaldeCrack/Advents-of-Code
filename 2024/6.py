# --- Day 6: Guard Gallivant ---
# https://adventofcode.com/2024/day/6
import re, copy


initial_guard_map: list[list[str]] = []
initial_guard_col: int
initial_guard_row: int
while row := list(input()):
	initial_guard_map.append(row)
	if match := re.search(r'\^|\>|\<|v', ''.join(row)):
		initial_guard_col = len(initial_guard_map) - 1
		initial_guard_row = match.start()
guard_map: list[list[str]] = copy.deepcopy(initial_guard_map)
guard_col: int = initial_guard_col
guard_row: int = initial_guard_row

directions: dict[str, tuple[int, int]] = {
	'^': (-1,  0),
	'>': ( 0,  1),
	'v': ( 1,  0),
	'<': ( 0, -1)
}
new_direction: dict[str, str] = {
	'^': '>',
	'>': 'v',
	'v': '<',
	'<': '^'
}

def in_bounds(col_pos: int, row_pos: int) -> bool:
	return 0 <= col_pos <= len(guard_map) - 1 and 0 <= row_pos <= len(guard_map[0]) - 1

while True:
	guard: str = guard_map[guard_col][guard_row]
	direction: tuple[int, int] = directions[guard]
	new_col, new_row = [sum(coords) for coords in zip((guard_col, guard_row), direction)]
	if in_bounds(new_col, new_row) and guard_map[new_col][new_row] == '#':
		guard_map[guard_col][guard_row] = new_direction[guard]
	else:
		guard_map[guard_col][guard_row] = 'X'
		guard_col = new_col
		guard_row = new_row
		if in_bounds(new_col, new_row): guard_map[new_col][new_row] = guard
		else: break

def in_loop(guard_map_: list[list[list[str]]], initial_state: str) -> bool:
	guard_col2: int = initial_guard_col
	guard_row2: int = initial_guard_row
	guard: str = initial_state
	while True:
		direction: tuple[int, int] = directions[guard]
		new_col, new_row = [sum(coords) for coords in zip((guard_col2, guard_row2), direction)]
		guard_map_[guard_col2][guard_row2].append(guard)
		if in_bounds(new_col, new_row) and guard_map_[new_col][new_row] == ['#']:
			guard = new_direction[guard]
		else:
			guard_col2 = new_col
			guard_row2 = new_row
			if not in_bounds(new_col, new_row): return False
		if guard in guard_map_[guard_col2][guard_row2]:
			return True

obstructions: int = 0
for i in range(len(guard_map)):
	for j in range(len(guard_map[i])):
		if guard_map[i][j] == 'X' and (i, j) != (initial_guard_col, initial_guard_row):
			guard_map_copy: list[list[list[str]]] = [(list(map(list, row)))
											for row in copy.deepcopy(initial_guard_map)]
			initial_state: str = guard_map_copy[initial_guard_col][initial_guard_row][0]
			guard_map_copy[initial_guard_col][initial_guard_row] = ['.']
			guard_map_copy[i][j] = ['#']
			obstructions += in_loop(guard_map_copy, initial_state)

visits: int = sum([len([cell for cell in row if cell == 'X']) for row in guard_map])
print(f'Part 1 solution: {visits}')
print(f'Part 2 solution: {obstructions}')
