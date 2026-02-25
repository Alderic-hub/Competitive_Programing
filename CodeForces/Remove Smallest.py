count = int(input())
for _ in range(count):
    vals = int(input())-1
    arr = list(map(int, input().split()))
    truth = True
    for n in range(vals, 0,-1):
        for y in range(n):
            if arr[n] < arr[y]:
                arr[y] , arr[n] = arr[n] , arr[y]
    for n in range(vals):
        diff = abs(arr[n] - arr[n+1])
        if diff != 0 and diff != 1:
            truth = False
            break
    if truth:
        print("Yes")
    else:
        print("No")
            
