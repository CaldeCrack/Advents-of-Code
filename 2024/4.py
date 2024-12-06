# --- Day 4: Ceres Search ---

word_search: list[str] = []

while line := input():
	word_search.append(line)

cols: int = len(word_search)
rows: int = len(word_search[0])

def check_xmas(i: int, j: int, di: int, dj: int) -> bool:
	return (0 <= i + 3 * di < cols
		and 0 <= j + 3 * dj < rows
		and word_search[i + 1 * di][j + 1 * dj] == 'M'
		and word_search[i + 2 * di][j + 2 * dj] == 'A'
		and word_search[i + 3 * di][j + 3 * dj] == 'S')

def check_x_mas(i: int, j: int, di: int, dj: int) -> bool:
	index: int = di + dj
	cross: str = 'MMSS'
	return (word_search[i + 1][j + 1] == cross[index]
		and word_search[i + 1][j - 1] == cross[(index + 1) % 4]
		and word_search[i - 1][j - 1] == cross[(index + 2) % 4]
		and word_search[i - 1][j + 1] == cross[(index + 3) % 4])

directions = [
	(-1,  0), # Up
	(-1,  1), # Up + Forward
	( 0,  1), # Forward
	( 1,  1), # Down + Forward
	( 1,  0), # Down
	( 1, -1), # Down + Backwards
	( 0, -1), # Backwards
	(-1, -1), # Up + Backwards
]

xmas_count: int = 0
x_mas_count: int = 0
for i in range(cols):
	for j in range(rows):
		if word_search[i][j] == 'X':
			for di, dj in directions:
				xmas_count += check_xmas(i, j, di, dj)
		if (1 <= i < cols - 1 and 1 <= j < rows - 1) and word_search[i][j] == 'A':
			for di, dj in directions[:4]:
				x_mas_count += check_x_mas(i, j, di, dj)

print(f'Part 1 solution: {xmas_count}')
print(f'Part 2 solution: {x_mas_count}')
