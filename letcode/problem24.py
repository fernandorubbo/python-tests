class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

class Problem24:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = head
        lp = None
        sp = head
        while head:
            head = head.next
            if head is None:
                break
            # swap value
            sp.next = head.next
            head.next = sp
            # fix link
            if lp is None:
                res = head
            else:
                lp.next = head
            # reposition pointers
            lp = sp
            head = sp.next
            sp = sp.next
        return res
