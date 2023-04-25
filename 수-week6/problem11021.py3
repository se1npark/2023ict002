T = int(input())
X = 0

for i in range(T):
    a, b = map(int, input().split())
    X += 1
    result = a + b
    print(f"Case #{X}: {result}")