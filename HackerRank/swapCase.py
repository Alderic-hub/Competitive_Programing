def swap_case(s):
    ans = []
    for item in s:
        if item.isupper():
            ans.append(item.lower())
        elif item.islower():
            ans.append(item.upper())
        else:
            ans.append(item)
    
    return ''.join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
