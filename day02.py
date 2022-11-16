# PART 1
def check_freq(x):
    return {c: x.count(c) for c in set(x)}


day2_input = [x.strip() for x in open("data/day02.txt", "r")]

count_two = 0
count_three = 0

for box in day2_input:
    frequencies = check_freq(box)
    count_two += 2 in frequencies.values()
    count_three += 3 in frequencies.values()

print(count_two * count_three)


# PART 2
first_box = ""
second_box = ""
current_common = 0
box_count = len(day2_input)
box_size = len(day2_input[0])
for i in range(box_count):
    for j in range(i + 1, box_count):
        common_count = 0
        for it in range(box_size):
            common_count += day2_input[i][it] == day2_input[j][it]
        if common_count > current_common:
            current_common = common_count
            first_box = day2_input[i]
            second_box = day2_input[j]

answer = ""
for it in range(box_size):
    if first_box[it] == second_box[it]:
        answer += first_box[it]

print(answer)
