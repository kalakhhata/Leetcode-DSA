import heapq
class Twitter:

    def __init__(self):
        self.tweet=defaultdict(list)
        self.following=defaultdict(set)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweet[userId].append([self.time,tweetId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap=[]
        res=[]
        user= self.following[userId] | {userId}
        for u in user:
            if self.tweet[u]:
                idx=len(self.tweet[u])-1
                time,tid=self.tweet[u][-1]
                heapq.heappush(max_heap,(-time,tid,u,idx))
        
        while max_heap and len(res)<10:
            _,tid,u,idx=heapq.heappop(max_heap)
            res.append(tid)
            if idx>0:
                idx=idx-1
                time,tid=self.tweet[u][idx]
                heapq.heappush(max_heap,(-time,tid,u,idx))
        
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)