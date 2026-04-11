# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp = head
        ans_list = []

        while temp:
            ans_list.append(temp.val)
            temp= temp.next
        ans_list.reverse()

        temp = head
        for num in ans_list:
            if num == temp.val:
                temp = temp.next
            else:
                return False
        return True

