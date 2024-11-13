class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Problem02:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Do exactly what we do with when doing math
        eg.
        incr:   0      1      0
                342     342     342
                465     465     465
                ----    ----    ----
                   7      07     807
        """
        num = ""
        incr = 0
        while l1 or l2 or incr!=0:
            v1 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            v2 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            sub = v1+v2+incr
            incr = sub // 10
            num = str(sub % 10) + num

        prev = None
        for n in num:
            l  = ListNode(int(n))
            if prev is not None:
                l.next = prev
            prev = l
        return l

    def addTwoNumbers_slower(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = str(self._reverse_num(l1) + self._reverse_num(l2))
        prev = None
        for n in num:
            l  = ListNode(int(n))
            if prev is not None:
                l.next = prev
            prev = l
        return l

    def _reverse_num(self, l):
        pointer = l
        num = ""
        while pointer is not None:
            num = str(pointer.val) + num
            pointer = pointer.next
        return int(num)
