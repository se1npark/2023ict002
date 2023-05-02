M = int(input())
N = int(input())

min_prime = -1

num_prime = 0
sum_prime = 0

for num in range(M, N+1):
    if num == 1:
        continue

    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        num_prime += 1
        sum_prime += num
        
        if min_prime == -1 or num < min_prime:
            min_prime = num

if num_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)