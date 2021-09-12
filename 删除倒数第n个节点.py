class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next =next

    def __str__(self):
        return  " val " + str(self.val)


if __name__ == '__main__':
    r = ListNode(1, ListNode(2))
    x=ListNode(-1)
    x.next = r

    src=x ;h=x;fast =x
    n=1
    while n>0 and fast.next:
        fast = fast.next
        n-=1

    while fast.next:
        fast = fast.next
        h = h.next

    if h.next:
        h.next = h.next.next
    print(x.next)