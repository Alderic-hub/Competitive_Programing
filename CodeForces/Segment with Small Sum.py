n, s = map(int, input().split())
arr = list(map(int, input().split()))
 
max_len = 0
current_sum = 0
start = 0
 
for end in range(n):
    current_sum += arr[end]
    while current_sum > s:
        current_sum -= arr[start]
        start += 1
    max_len = max(max_len, end - start + 1)
 
print(max_len)
