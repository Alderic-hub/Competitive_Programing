n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))
if k == 0:
    val = arr[0]-1
    if val >= 1:
        print(val)
    else:
        print(-1)
elif k == 1:
    if n > 1:
        if arr[0] == arr[1]:
            print(-1)
        else:
            print(arr[0])
    else:
        print(arr[0])
elif k < n:
    if arr[k] == arr[k-1]:
        print(-1)
    else:
        print(arr[k-1])
else:
    print(arr[n-1])
