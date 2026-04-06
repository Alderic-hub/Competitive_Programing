# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ans = False 
        temp = head

        while temp:
            if temp.val == "#":
                ans = True
                break
            else:
                temp.val = "#"
                temp = temp.next
        return ans
        
