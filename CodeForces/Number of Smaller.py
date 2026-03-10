length = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ans = []
point = 0
num = 0
for n in arr2:
    while point <  length[0]:
        if arr1[point] >= n:
            break
        num += 1
        point += 1
    ans.append(num)
    
print(ans)
