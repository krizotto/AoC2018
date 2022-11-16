# PART 1


def check_freq(x):
    return {c: x.count(c) for c in set(x)}


day2_input = [x for x in open("data/day02test.txt", "r")]

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
current_distinguish = 1000
for i in range(len(day2_input)):
    for j in range(i + 1, len(day2_input)):
        temp_distinguish = 0
        for it in range(len(day2_input[i])):
            temp_distinguish += day2_input[i][it] == day2_input[j][it]
        if temp_distinguish < current_distinguish:
            current_distinguish = temp_distinguish
            first_box = day2_input[i]
            second_box = day2_input[j]

answer = ""
for it in range(len(first_box)):
    if first_box[it] == second_box[it]:
        answer += first_box[it]

print(answer)
