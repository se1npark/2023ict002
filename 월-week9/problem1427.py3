N = int(input())  

digits = list(str(N))
digits.sort(reverse=True)

result = ''.join(digits)
sorted_num = int(result)

print(sorted_num)