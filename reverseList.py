def reverse(head, m, n):
    for _ in range(2, m):
        head = head.next
    temp = head
    tempNext = temp.next
    for _ in range (n - m):
        head = head.next
    nextTemp = head
    nextNextTemp = nextTemp.next
    head = temp.next
    while head != nextTemp:
        tempHead = head
        head = head.next
        nextNode = head.next
        nextNode.next = tempHead
    temp.next = nextTemp
    tempNext.next = nextNextTemp
    return temp
    