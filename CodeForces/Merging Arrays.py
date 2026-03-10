length = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ans = []
point1 = 0
point2 = 0
while point1 < length[0]:
    if point2 < length[1]:
        if arr1[point1]>arr2[point2]:
            ans.append(arr2[point2])
            point2 +=1
        else:
            ans.append(arr1[point1])
            point1 +=1
    else:
        break
if point1 != length[0]:
    ans.extend(arr1[point1:])
if point2 != length[1]:
    ans.extend(arr2[point2:])
print(ans)
