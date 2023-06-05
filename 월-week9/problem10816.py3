N = int(input())
cards = list(map(int, input().split()))

card_count = {}
for i in cards:
    if i in card_count:
        card_count[i] += 1
    else:
        card_count[i] = 1


M = int(input())
targets = list(map(int, input().split()))

for j in targets:
    if j in card_count:
        print(card_count[j], end=' ')
    else:
        print(0, end=' ')