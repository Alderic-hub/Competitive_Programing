vals = list(map(int, input().split()))
birr = 0
for n in range(1,vals[2]+1):
    birr += n*vals[0]
if vals[1] > birr:
    print(0)
else:
    print(birr - vals[1])
