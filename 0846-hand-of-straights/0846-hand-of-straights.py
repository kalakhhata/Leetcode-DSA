class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand)%groupSize!=0:
            return False
        
        count = Counter(hand)

        for card in sorted(count):
            freq=count[card]
            if freq>0:
                for next_el in range(card,card+groupSize):
                    if count[next_el]<freq:
                        return False
                    count[next_el]-=freq
        
        return True
        