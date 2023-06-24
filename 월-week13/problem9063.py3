N = int(input())
x_set = set()
y_set = set()

for i in range(N):
    x, y = map(int, input().split())
    x_set.add(x)
    y_set.add(y)

print((max(x_set) - min(x_set)) * (max(y_set) - min(y_set)))