import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())  

    while True:
        if is_prime(n):
            print(n)
            break
        n += 1