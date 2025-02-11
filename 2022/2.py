# --- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

scores: dict[str, int] = {
	"A": 1, # Rock
	"B": 2, # Paper
	"C": 3, # Scissors
	"X": 1, # Rock
	"Y": 2, # Paper
	"Z": 3, # Scissors
}
rounds: list[list[str]] = []
while strategy := input():
	rounds.append(strategy.split())
plays: list[int] = [3 * ((scores[play[1]] - scores[play[0]] + 1) % 3) + scores[play[1]] for play in rounds]
new_plays: list[int] = [(scores[play[1]] + scores[play[0]]) % 3 - 2 + 3 * scores[play[1]] for play in rounds]

print(f'Part 1 solution: {sum(plays)}')
print(f'Part 2 solution: {sum(new_plays)}')
