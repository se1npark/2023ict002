A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C

hour = total // 60
minute = total % 60

hour %= 24

print(hour, minute)