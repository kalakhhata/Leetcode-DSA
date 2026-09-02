class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Merge two halves
        first = head
        second = prev

        while first and second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2