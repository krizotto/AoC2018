from collections import Counter
import re


def process(claim: str):
    if claim == "":
        return []
    returnlist = []
    claim_id, x, y, range_x, range_y = list(
        filter(None, re.split("  | |@|,|:|x", claim))
    )
    x = int(x)
    y = int(y)
    range_x = int(range_x)
    range_y = int(range_y)
    for i in range(range_x):
        for j in range(range_y):
            returnlist.append((x + i, y + j))
    return returnlist, claim_id


points = []
input = [x.strip() for x in open("data/day03.txt", "r")]
for claim in input:
    curr_points, claim_ids = process(claim)
    points.extend(curr_points)
counter_dict = dict(Counter(points)).items()
points_more_than_one = [p for p, cnt in counter_dict if cnt > 1]

print(len(points_more_than_one))
# freq = check_freq(points)

# PART 2
for claim in input:
    curr_points, claim_ids = process(claim)
    distinct = True
    for p in curr_points:
        if p in points_more_than_one:
            distinct = False
            break
    if distinct:
        print(claim_ids)
        break
