N, M = map(int, input().split())

baskets = list(range(1, N+1))

for x in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)