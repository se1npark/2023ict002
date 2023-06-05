N = int(input())
X = list(map(int, input().split()))

ap = [(X[i], i) for i in range(N)]
ap.sort()

result = [0] * N

count = 0
for i in range(N):
    if i > 0 and ap[i][0] != ap[i-1][0]:
        count += 1
    result[ap[i][1]] = count

print(' '.join(map(str, result)))