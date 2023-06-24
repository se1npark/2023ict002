A, B = map(int, input().split())
max_num = max(A, B)

for lcm in range(max_num, A * B + 1, max_num):
    if lcm % A == 0 and lcm % B == 0:
        break

print(lcm)