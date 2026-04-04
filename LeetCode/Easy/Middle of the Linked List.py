
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = head
        ans = []
        count = 0
        while val:
            ans.append(val.val)
            val = val.next
            count += 1
        count = int(count/2) 
        temp = head
        for _ in range(count):
            temp = temp.next
        return temp
v
