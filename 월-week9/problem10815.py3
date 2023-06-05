N = int(input())
have_num = set(map(int, input().split()))

M = int(input())
ornot_num = list(map(int, input().split()))

for num in ornot_num:
  if num in have_num:
    print(1, end=' ')
  else:
    print(0, end=' ')