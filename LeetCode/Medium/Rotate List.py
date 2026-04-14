# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        if count <2:
            return head
            
        temp = head
        while temp.next:
            temp=temp.next
        temp.next = head


        temp = head
        value = k
        if count < k:
            value = k%count
            
        for _ in range(count-value):
            temp = temp.next
        answer = temp
        while temp.next != answer:
            temp = temp.next

        temp.next = None
        return answer


        
