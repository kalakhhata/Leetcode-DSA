class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        events=[]
        for passenger,pu,do in trips:
            events.append((pu,passenger))
            events.append((do,-passenger))
        
        events.sort()
        total=0
        for loc,passenger in events:
            total+=passenger
            if total>capacity:
                return False
        return True
