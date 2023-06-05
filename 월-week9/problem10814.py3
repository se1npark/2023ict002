N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))

sorted_members = sorted(members, key=lambda x: (x[0], x[2]))

for member in sorted_members:
    print(member[0], member[1])
