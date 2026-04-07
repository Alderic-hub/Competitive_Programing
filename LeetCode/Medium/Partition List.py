# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        small = []
        high = []
        for val in arr:
            if val < x:
                small.append(val)
            else:
                high.append(val)

        ans_list = small + high
        temp = head
        for value in ans_list:
            temp.val = value
            temp = temp.next
        
        return head

