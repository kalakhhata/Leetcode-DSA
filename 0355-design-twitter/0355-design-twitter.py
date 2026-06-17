import heapq
class Twitter:

    def __init__(self):
        self.tweet=defaultdict(list)
        self.followi=defaultdict(set)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        max_heap=[]
        res=[]
        users = self.followi[userId] | {userId}

        for u in users:
            if self.tweet[u]:
                idx=len(self.tweet[u])-1
                time,tId=self.tweet[u][idx]
                heapq.heappush(max_heap,(-time,idx,u,tId))
        
        while max_heap and len(res)<10:
            t,idx,u,tId=heapq.heappop(max_heap)
            res.append(tId)
            if idx-1 >= 0:
                idx=idx-1
                t,tId=self.tweet[u][idx]
                heapq.heappush(max_heap,(-t,idx,u,tId))
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followi[followerId].add(followeeId)


        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followi[followerId].discard(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)