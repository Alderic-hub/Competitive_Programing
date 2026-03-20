n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
cur = 0
ans = 0

for right in range(n):
    cur += arr[right]
    
    while cur > t:
        cur -= arr[left]
        left += 1
    
    ans = max(ans, right - left + 1)

print(ans)
