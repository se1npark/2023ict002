white_pieces = list(map(int, input().split()))
black_pieces = [1, 1, 2, 2, 2, 8]

for i in range(len(white_pieces)):
    print(black_pieces[i] - white_pieces[i], end=' ')