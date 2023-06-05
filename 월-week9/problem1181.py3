N = int(input())
words = []
for _ in range(N):
    word = input()
    words.append(word)

sorted_words = sorted(set(words), key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)