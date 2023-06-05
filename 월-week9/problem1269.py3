n, m = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

daeCha = len(A-B) + len(B-A)


print(daeCha)