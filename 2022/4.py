# --- Day 4: Camp Cleanup ---
# https://adventofcode.com/2022/day/4

contained: int = 0
overlapped: int = 0
while elf_pair := input():
	ranges_text: list[str] = elf_pair.split(",")
	first_range: list[int] = [int(bound) for bound in ranges_text[0].split("-")]
	second_range: list[int] = [int(bound) for bound in ranges_text[1].split("-")]
	x1, x2, y1, y2 = *first_range, *second_range
	if (x2 >= y1 and x1 <= y2) or (y2 >= x1 and y1 <= x2):
		overlapped += 1
		if (y1 <= x1 and x2 <= y2) or (x1 <= y1 and y2 <= x2):
			contained += 1

print(f'Part 1 solution: {contained}')
print(f'Part 2 solution: {overlapped}')
