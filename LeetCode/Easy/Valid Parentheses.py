class Solution(object):
    def isValid(self, s):
        end = [']', '}',')']
        arr = []
        for items in s:
            if items not in end:
                arr.append(items)
            else:
                if arr:
                    if items == ']' and arr[-1] == '[':
                        arr.pop()
                    elif items == '}' and arr[-1] == '{':
                        arr.pop()
                    elif items == ')' and arr[-1] == '(':
                        arr.pop()
                    else:
                        return  False
                else:
                    return False

        if arr:
            return False
        return True
        
            
               
