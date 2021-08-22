import copy


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next =next

    def __str__(self):
        return  " val " + str(self.val)


def reverseGroup(r , b):
    hd = None ;  c2 = r
    while c2 and c2 != b:
        t = c2.next
        c2.next = hd
        hd = c2
        c2 = t
    return hd

if __name__ == '__main__':

    r =  ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6,ListNode(7,ListNode(8))))))))
    ## 单链表反转
    r2 = copy.deepcopy(r)
    k = None
    n = r2
    while n:
        nx = n.next
        n.next = k
        k = n
        n = nx

    print(k)
    ## 单链表反转


    # hd = ListNode(-1, r)
    N = 3
    pt= t =  hd = cr = r
    k = N - 1
    while cr:
        k -= 1
        cr = cr.next
        if cr == None:
            break
        if k == 0:
           cr = cr.next
           #临时头节点 chd 临时尾节点
           hd2 = reverseGroup(t, cr)
           pt.next = hd2
           pt = t
           if hd == r:
               hd = hd2
           t.next = cr
           t = cr
           k = N-1

    print(hd)
