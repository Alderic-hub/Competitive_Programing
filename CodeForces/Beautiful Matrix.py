tot_val = []
for _ in range(5):
    val = list(map(int,input().split()))
    tot_val.append(val)
count = 0
for items in tot_val:
    if 1 in items:
        row = count
        column = items.index(1)
    count += 1
ans = abs(2-row) + abs(2-column)

print(ans)
   
