import heapq

class MedianFinder(object):

    def __init__(self):
        self.left = []   # max heap (negated values)
        self.right = []  # min heap

    def addNum(self, num):
        # Step 1: push into correct heap
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # Step 2: rebalance sizes (difference ≤ 1)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

        # Step 3: fix ordering if violated
        if self.left and self.right and -self.left[0] > self.right[0]:
            l = -heapq.heappop(self.left)
            r = heapq.heappop(self.right)
            heapq.heappush(self.left, -r)
            heapq.heappush(self.right, l)

    def findMedian(self):
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return float(-self.left[0])
        else:
            return float(self.right[0])
