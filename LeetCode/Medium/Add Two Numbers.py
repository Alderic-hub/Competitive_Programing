# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        
        arr1 = []
        while temp1:
            arr1.append(str(temp1.val))
            temp1 = temp1.next
            
        arr2 = []
        while temp2:
            arr2.append(str(temp2.val))
            temp2 = temp2.next
        arr1.reverse()  
        arr2.reverse()

        str1 = int("".join(arr1))
        str2 = int("".join(arr2))
        
        res = str1 + str2
        
        str3 = str(res)
        print(str3)
        
        head = ListNode(int(str3[-1]))
        temp = head
        for value in range(len(str3) - 2, -1, -1):
            new_node = ListNode(int(str3[value]))
            temp.next = new_node
            temp = temp.next
            
        return head  
        
        
