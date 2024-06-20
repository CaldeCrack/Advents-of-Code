# First Star
data = open("data.txt", "r") # I won't ever care to close files
rounds, scores= [matches.strip().split(" ") for matches in data.readlines()], {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
results = [(3*((scores[play[1]]-scores[play[0]]+1)%3) + scores[play[1]]+1) for play in rounds]

#Second Star
results2 = [((scores[play[1]]+scores[play[0]]-1)%3+1 + 3*scores[play[1]]) for play in rounds]
print("first sum:" , str(sum(results)) + ", second sum:" , str(sum(results2)))