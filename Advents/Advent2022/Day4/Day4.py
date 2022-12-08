# First Star
data, n1, n2 = open("data.txt", "r"), 0, 0
pairs = [pair.strip().split(",") for pair in data.readlines()]
ranges = [[pair[0].split("-"), pair[1].split("-")] for pair in pairs]
for pair in ranges:
    x1, x2, y1, y2 = int(pair[0][0]), int(pair[0][1]), int(pair[1][0]), int(pair[1][1])
    if (y1 <= x1 and x2 <= y2) or (x1 <= y1 and y2 <= x2): (n1,n2) = (n1+1,n2+1)
    # Second Star
    elif (x2 >= y1 and x1 <= y2) or (y2 >= x1 and y1 <= x2): n2 += 1
print("contained:" , str(n1) + ", overlapped:" , str(n2))