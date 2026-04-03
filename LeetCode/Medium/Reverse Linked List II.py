
class Solution(object):
    def reverseBetween(self, head, left, right):
        left_val = head
        ans_list = []
        for _ in range(left-1):
            left_val = left_val.next
        
        if left != 0:
            end = right - left + 1 
        else:
            end = right
        ans_link = left_val
        for _ in range(end):
            if left_val:
                ans_list.append(left_val.val)
                left_val = left_val.next

        ans_list.reverse()
        for num in ans_list:
            ans_link.val = num
            ans_link = ans_link.next

        return head

