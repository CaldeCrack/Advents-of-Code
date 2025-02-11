# --- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1

calories: list[int] = []
n: int = 0
while True:
	calorie: str = input()
	if not calorie:
		if n == 0:
			break
		calories.append(n)
		n = 0
		continue
	n += int(calorie)

calories.sort()
print(f'Part 1 solution: {calories[-1]}')
print(f'Part 2 solution: {sum(calories[-3:])}')
