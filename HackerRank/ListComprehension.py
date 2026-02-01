if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = []
    for itemx in range(x+1):
        for itemy in range(y+1):
            for itemz in range(z+1):
                sum = itemx + itemy + itemz
                if sum != n:
                    arr = [itemx, itemy, itemz]
                    ans.append(arr)
    print(ans)
              
