# --- Day 5: Print Queue ---
# https://adventofcode.com/2024/day/5

rules: dict[int, list[int]] = {}
while rule := list(map(int, input().replace('|', ' ').split())):
	if rules.get(rule[0]): rules[rule[0]].append(rule[1])
	else: rules[rule[0]] = [rule[1]]

total: int = 0
corrected_total: int = 0
while update := list(map(int, input().replace(',', ' ').split())):
	valid: bool = True
	last_appearance: dict[int, int] = {}
	for i, page in enumerate(update):
		last_appearance[page] = i
		for rule in rules.get(page, []):
			valid &= last_appearance.get(rule, -1) == -1
		if not valid: break
	total += valid * update[len(update) // 2]

	if not valid:
		last_appearance.clear()
		i: int = 0
		while i < len(update):
			last_appearance[update[i]] = i
			for rule in rules.get(update[i], []):
				if (index := last_appearance.get(rule, -1)) != -1:
					update[i], update[index] = update[index], update[i]
					last_appearance.clear()
					i = -1
					break
			i += 1
		corrected_total += update[len(update) // 2]

print(f'Part 1 solution: {total}')
print(f'Part 2 solution: {corrected_total}')
