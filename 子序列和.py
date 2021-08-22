import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        hd = rst =  ListNode(-1)
        up = 0
        while True:


            sum =  l1.val if l1  else 0
            sum +=  l2.val if l2  else 0
            sum += up

            up = int(sum / 10)
            sum = sum % 10
            rst.next = ListNode(sum)
            rst = rst.next

            if not l1 and not l2:
                break

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return hd.next
def arr2list(a) -> ListNode:
    head = b = ListNode(a[0])
    for i in a[1:]:
        b .next = ListNode(i)
        b = b.next
    return head

def plist(b : ListNode) :
    if not b:
        return
    print(b.val , " ")
    plist(b.next)

if __name__ == '__main__':
    plist(Solution().addTwoNumbers(arr2list([9,9,9,9,9,9,9]),
                                   arr2list([9,9,9,9])))