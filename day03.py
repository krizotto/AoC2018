from collections import Counter
import re

def process(claim: str):
    returnlist = []
    claim_id, x, y, range_x, range_y = list(
        filter(None, re.split("  | |@|,|:|x", claim))
    )
    x, y, range_x, range_y = int(x), int(y), int(range_x), int(range_y)
    for i in range(range_x):
        for j in range(range_y):
            returnlist.append((x + i, y + j))
    return set(returnlist), claim_id


input = [x.strip() for x in open("data/day03.txt", "r")]

# PART 1
points = []
for claim in input:
    curr_points, claim_id = process(claim)
    points.extend(curr_points)
points_more_than_one = [p for p, cnt in dict(Counter(points)).items() if cnt > 1]

print(len(points_more_than_one))

# PART 2
for claim in input:
    curr_points, claim_id = process(claim)
    if curr_points.isdisjoint(points_more_than_one):
        print(claim_id)
        break
