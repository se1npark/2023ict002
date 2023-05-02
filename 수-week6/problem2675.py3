t=int(input())

for i in range(t):
    r, s = input().split()

    p = ""
    for alph in s:
        p += alph*int(r)

    print(p)