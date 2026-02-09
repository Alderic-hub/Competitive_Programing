count = int(input())
for _ in range(count):
    word = input()
    val = len(word)
    if val > 10:
        val -= 2
        print(f'{word[0] }{ val }{ word[val+1]}')
    else:
        print(word)
