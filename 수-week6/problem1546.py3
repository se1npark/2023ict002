N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
new_scores = []

for i in scores:
    new_score = i / max_score * 100
    new_scores.append(new_score)

avg = sum(new_scores) / N
print(avg)