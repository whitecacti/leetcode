from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = ListNode()
    new_one = dummy

    if not head:
        return None

    while head and head.next:
        if head.val == head.next.val:
            print('same', head.val)
            head = head.next
        else:
            print('adding', head.val)
            new_one.next = ListNode(head.val)
            new_one = new_one.next 
            head = head.next

    if head:
        new_one.next = ListNode(head.val)

    return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(3)
    f = ListNode(3)

    # a = ListNode(-1)
    # b = ListNode(0)
    # c = ListNode(0)
    # d = ListNode(0)
    # e = ListNode(3)
    # f = ListNode(3)

    a.next = b
    a.next.next = c
    a.next.next.next = d
    a.next.next.next.next = e
    a.next.next.next.next.next = f

    head = deleteDuplicates(a)
    print(head.val)
    print(head.next.val)
    print(head.next.next.val)
    