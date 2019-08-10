class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def countList(head):
    count = 1
    while (head.next != None):
        head = head.next
        count += 1
    return count

def check(head, mid1, mid2):
    secondHead = head
    for _ in range(mid2):
        secondHead = secondHead.next
    if mid1 == 0:
        head.next = None
    else:
        count = 0
        privious = None
        nextNode = None
        while (count != mid1):
            nextNode = head.next
            head.next = privious
            privious = head
            head = nextNode
            count += 1
        head.next = privious
    
    while (head != None):
        if head.val != secondHead.val:
            return False
        head = head.next
        secondHead = secondHead.next
    return True



def isPalindrom(head):
    if head.next == None:
        return True
    second = head.next
    if second.next == None:
        if second.val == head.val:
            return True
        else: return False
    size = countList(head)
    mid = size // 2
    if size % 2 == 1:
        return check(head, mid - 1, mid + 1)
    else:
        return check(head, mid - 1, mid)
    

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head4 = ListNode(2)
head4.next = ListNode(1)
head.next.next.next = head4

print(isPalindrom(head))