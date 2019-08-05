def detectCycle(head):
    headOne = head[0]
    headTwo = head[0]
    if headTwo.next == None:
        return None
    if headTwo.next == headOne:
        return 0
    if headTwo.next.next == None:
        return None
    headTwo = headTwo.next.next

    while (headOne != None and headTwo != None and headTwo.next != None):
        if headOne == headTwo:
            break
        headOne = headOne.next
        if headTwo.next.next == None:
            headOne = None
            break
    if headOne:
        countForward = 0
        countFromStart = 0
        while(headTwo != headOne):
            headTwo = headTwo.next
            countForward += 1
        headTwo = head[0]
        while(headTwo != headOne):
            headTwo = headTwo.next
            countForward += 1
        return abs(countForward - countFromStart)
    else:
        return None
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        headOne = head
        headTwo = head
        if headTwo.next == None:
            return None
        if headTwo.next == headOne:
            return 0
        if headTwo.next.next == None:
            return None
        headTwo = headTwo.next.next
        while (headOne != None and headTwo != None and headTwo.next != None):
            if headOne == headTwo:
                break
            headOne = headOne.next
            if headTwo.next.next == None:
                headOne = None
                break
            headTwo = headTwo.next.next
        if headOne:
            countForward = 0
            countFromStart = 0
            while(headTwo != headOne):
                headTwo = headTwo.next
                countForward += 1
            headTwo = head
            while(headTwo != headOne):
                headTwo = headTwo.next
                countForward += 1
            return abs(countForward - countFromStart)
        else:
            return None