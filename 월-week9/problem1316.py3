N = int(input())
group_count = 0

for _ in range(N):
    word = input()
    prev_char = ''
    used_chars = set()
    is_group_word = True
    
    for char in word:
        if char != prev_char:
            if char in used_chars:
                is_group_word = False
                break
            used_chars.add(char)
        prev_char = char
    
    if is_group_word:
        group_count += 1

print(group_count)
