word = input().lower()

counts = {}
max_count = 0

for alph in word:
        if alph in counts:
            counts[alph] += 1
        else:
            counts[alph] = 1

        if counts[alph] > max_count:
            max_count = counts[alph]

most_common = []
for alph, count in counts.items():
    if count == max_count:
        most_common.append(alph)

if len(most_common) == 1:
    result = most_common[0].upper()
else:
    result = '?'

print(result)