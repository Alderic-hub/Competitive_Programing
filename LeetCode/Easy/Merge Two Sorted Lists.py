
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ans = None
        head = None
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val < list2.val:
                if ans == None:
                    ans = list1
                    head = ans
                else:
                    ans.next = list1
                    ans = ans.next
                list1 = list1.next
            else:
                if ans == None:
                    ans = list2
                    head = ans
                else:
                    ans.next = list2
                    ans = ans.next
                list2 = list2.next
        if list1:
            while list1:
                ans.next = list1
                ans = ans.next
                list1 = list1.next
        if list2:
            while list2:
                ans.next = list2
                ans = ans.next
                list2 = list2.next
        return head
        
