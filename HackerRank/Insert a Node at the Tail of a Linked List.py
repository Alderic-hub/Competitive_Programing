
def insertNodeAtTail(head, data):
    val = SinglyLinkedListNode(data)
    if not head:
        return val
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = val
    return head
    
      

