N, M = map(int, input().split()) 

unheard = set()
unseen = set()

for _ in range(N):
    name = input().strip()
    unheard.add(name)

for _ in range(M):
    name = input().strip()
    unseen.add(name)

both = unheard & unseen 
count = len(both)


sorted_list = sorted(both)

print(count) 
for name in sorted_list:
    print(name)