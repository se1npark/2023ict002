def program(s):
    n = len(s)
    str = set()

    for i in range(n):
        for j in range(i+1, n+1):
            str.add(s[i:j])

    return len(str)

s = input()

result = program(s)
print(result)