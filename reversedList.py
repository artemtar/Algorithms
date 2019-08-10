def helper(head):
    if head.next == None:
        return head, head
    else:
        nextNode, hh = helper(head.next)
        nextNode.next = head
        return head, hh

def reversedList(head):
    if head == None:
        return head
    privious = None
    while (head.next != None):
        temp = head.next
        head.next = privious
        head = temp 
    return head

