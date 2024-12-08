# --- Day 7: Bridge Repair ---
# https://adventofcode.com/2024/day/7

def numberToBase(n: int, b: int) -> str:
    if n == 0: return '0'
    digits: list[int] = []
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join([str(digit) for digit in digits[::-1]])

def operation_n_mask(length: int, base: int = 2):
	limit: int = base ** length
	i: int = 0
	while True:
		n: str = f'{numberToBase(i, base).zfill(length)}'
		yield n
		i = (i + 1) % limit

operation_map: dict[str, str] = {
	'0': '+',
	'1': '*',
	'2': '||',
}

total2: int = 0
total3: int = 0
while operation := list(map(int, input().replace(':', '').split())):
	result = operation[0]
	operands = operation[1:]
	operations_amount: int = len(operands) - 1
	mask_2_generator = operation_n_mask(operations_amount)
	limit: int = 2 ** operations_amount
	i: int = 0
	while i < limit:
		mask: str = next(mask_2_generator)
		tmp_result: int = operands[0]
		for j, operation in enumerate(mask):
			tmp_result = (tmp_result + operands[j + 1]) if operation_map[operation] == '+' else tmp_result * operands[j + 1]
		if tmp_result == result:
			total2 += result
			break
		i += 1

	mask_3_generator = operation_n_mask(operations_amount, 3)
	limit = 3 ** operations_amount
	i = 0
	while i < limit:
		mask: str = next(mask_3_generator)
		tmp_result: int = operands[0]
		for j, operation in enumerate(mask):
			if operation_map[operation] == '+':
				tmp_result += operands[j + 1]
			elif operation_map[operation] == '*':
				tmp_result *= operands[j + 1]
			else:
				tmp_result = int(str(tmp_result) + str(operands[j + 1]))
		if tmp_result == result:
			total3 += result
			break
		i += 1

print(f'Part 1 solution: {total2}')
print(f'Part 2 solution: {total3}')
