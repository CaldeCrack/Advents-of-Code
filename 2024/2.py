# --- Day 2: Red-Nosed Reports ---

def check_safe(report: list[int]) -> bool:
	increasing = report[0] < report[1]
	for j in range(len(report) - 1):
		diff = report[j] - report[j + 1]
		if ((diff < 0) != increasing) or (not 1 <= abs(diff) <= 3):
			return False
	return True

safe1: int = 0
safe2: int = 0
while report := list(map(int, input().split())):
	damp: int = 2
	increasing: bool = report[0] < report[1]
	for i in range(len(report) - 1):
		diff: int = report[i] - report[i + 1]
		if ((diff < 0) != increasing) or (not 1 <= abs(diff) <= 3):
			damp -= 1
			new_report1: list[int] = [level for j, level in enumerate(report) if j != i]
			new_report2: list[int] = [level for j, level in enumerate(report) if j != i + 1]
			new_report3: list[int] = [level for j, level in enumerate(report) if j != (i - 1 if i else i)]
			damp -= not (check_safe(new_report1) or check_safe(new_report2) or check_safe(new_report3))
			break
	safe1 += damp == 2
	safe2 += bool(damp)

print(f'Part 1 solution: {safe1}')
print(f'Part 2 solution: {safe2}')
