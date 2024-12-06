# --- Day 3: Mull It Over ---

import re

total: int = 0
conditional_total: int = 0
do: bool = True
while corrupted_memory := input():
	matches: list[str] = re.findall(r'mul\(\d+,\d+\)', corrupted_memory)
	numbers: list[list[int]] = list(map(lambda mul: list(map(int, re.findall(r'\d+', mul))), matches))
	total += sum(map(lambda mul: mul[0] * mul[1], numbers))

	matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", corrupted_memory)
	for match in matches:
		do = (match == 'do()' or ((not match == "don't()") and do))
		if do and match[:3] == 'mul':
			numbers: list[str] = match.replace('mul(', '').replace(')', '').split(',')
			conditional_total += int(numbers[0]) * int(numbers[1])

print(f'Part 1 solution: {total}')
print(f'Part 2 solution: {conditional_total}')
