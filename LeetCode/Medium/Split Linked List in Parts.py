# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        ans = []
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
        
        value = count // k
        extra = count % k
        counter = k
        temp = head
        
        while counter:
            if temp:
                ans.append(temp)
                if extra:
                    co = value + 1
                    extra -= 1
                else:
                    co = value
                while co > 1:
                    temp = temp.next
                    co -= 1
                nextt = temp.next
                temp.next = None
                temp = nextt
            else:
                ans.append(None)
            
            counter -= 1
        
        return ans
