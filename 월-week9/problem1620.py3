import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_dict = {}

for i in range(1, n + 1):
    pokemon = input().rstrip()
    pokemon_dict[str(i)] = pokemon
    pokemon_dict[pokemon] = str(i)

for i in range(m):
    question = input().rstrip()
    if question in pokemon_dict:
        print(pokemon_dict[question])
    elif question.isdigit() and int(question) in pokemon_dict:
        print(pokemon_dict[int(question)])