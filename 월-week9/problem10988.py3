def findP(word):
    n = len(word)
    for i in range(n//2):
        if word[i] != word[n-1-i]:
            return 0
    return 1

word = input()
result = findP(word)

print(result)