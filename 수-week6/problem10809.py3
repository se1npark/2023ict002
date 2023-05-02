S=input()
alpha=list('abcdefghijklmnopqrstuvwxyz')
result=[-1] * 26

for i in range(len(S)):
    if S[i] in alpha:
        idx = alpha.index(S[i])
        if result[idx] == -1:
            result[idx] = i

for i in result:
    print(i, end=' ')