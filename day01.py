day1_input = [int(x) for x in open("data/day01.txt", "r")]
# PART 1
print(sum(day1_input))

# PART 2
p2_output = 0
p2_set = {0}
index = 0
while True:
    p2_output += day1_input[index % len(day1_input)]
    if p2_output in p2_set:
        break
    else:
        p2_set.add(p2_output)
        index += 1
print(p2_output)
