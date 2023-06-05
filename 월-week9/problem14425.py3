n, m = map(int, input().split())

S = set()
for _ in range(n):
    word = input()
    S.add(word)

count = 0
for _ in range(m):
    word = input().rstrip()
    if word in S:
        count += 1

print(count)