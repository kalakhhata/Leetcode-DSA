class Twitter:

    def __init__(self):
        self.followe=defaultdict(set)
        self.tweet=defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> list[int]:
        res=[]
        heap=[]
        users= self.followe[userId] | {userId}

        for u in users:
            if self.tweet[u]:
                idx=len(self.tweet[u])-1
                time,tid=self.tweet[u][idx]
                heapq.heappush(heap,(-time,idx,tid,u))
        
        while heap and len(res)<10:
            time,idx,tid,u = heapq.heappop(heap)
            res.append(tid)
            if idx-1>=0:
                idx=idx-1
                time,tid=self.tweet[u][idx]
                heapq.heappush(heap,(-time,idx,tid,u))
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followe[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followe[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)