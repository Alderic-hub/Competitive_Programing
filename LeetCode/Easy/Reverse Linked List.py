
class Solution(object):
    def reverseList(self, head):
        ans_list = []
        ans = None
        val = head
        while val:
            ans_list.append(val.val)
            val = val.next
        ans_list.reverse()
        cur = head
        for num in ans_list:
            cur.val = num 
            cur = cur.next
        return head
