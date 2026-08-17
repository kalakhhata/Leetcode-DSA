class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        beforeLeft = None
        curr = head

        for _ in range(left - 1):
            beforeLeft = curr
            curr = curr.next

        prev = None
        cleft = curr
        cnt = 0

        while curr and cnt < right - left + 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            cnt += 1

        if beforeLeft:
            beforeLeft.next = prev
        else:
            head = prev  # Reversal started at the original head

        cleft.next = curr

        return head