def reorder(head):
    if not head:
        return None
    if not head.next:
        return head
    tail = None
    headReversed = head.next
    headReversed.next = None 
    while head != None:
        if head.next.next == None:
            tail = headReversed
            break
        nextHead = head.next.next
        if not nextHead.next:
            tail = headReversed
            break
        else:
            temp = nextHead.next
            temp.next = headReversed
            headReversed = temp
    
        
        

