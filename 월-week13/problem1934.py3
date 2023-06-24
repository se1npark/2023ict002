T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    product = A * B

    if A > B:
        larger = A
        smaller = B
    else:
        larger = B
        smaller = A

    while smaller != 0:
        remainder = larger % smaller
        larger = smaller
        smaller = remainder

    lcm = product // larger
    print(lcm)