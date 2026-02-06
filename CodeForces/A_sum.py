count = int(input())
for n in range(count):
    num_list = sorted(map(int,input().split()))
    if num_list[2] - num_list[1] == num_list[0]:
        print("Yes")
    else:
        print("No")
