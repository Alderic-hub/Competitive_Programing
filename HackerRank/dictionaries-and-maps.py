
num = int(input())
ans = dict()

for n in range(num):
    arr = input().split()
    ans[arr[0]] = arr[1]

while True:
    try:
        val = input()
        if val in ans:
            print(f'{val}={ans[val]}')
        else:
            print('Not found')
    except EOFError:
        break
