N, k = map(int, input().split())

x = list(map(int, input().split()))
x.sort(reverse=True)

cut_line = x[k-1]

print(cut_line)