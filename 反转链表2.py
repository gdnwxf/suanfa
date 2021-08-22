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
def findK (r :ListNode, k):
    hd = r
    for i in range(0,k):
        if not r:
            # 如果r为空 还没有到K个 则直接返回hd
            return hd
        r = r.next
    # 反转出来的hd是新的head
    n_hd= reverseGroup(hd, r)
    hd.next = findK(r, k)
    return n_hd
if __name__ == '__main__':

    r =  ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5, ListNode(6,ListNode(7,ListNode(8))))))))
    hd= findK(r,3)
    print(hd)
