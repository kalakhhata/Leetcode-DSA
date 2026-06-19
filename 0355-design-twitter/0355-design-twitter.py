import heapq
class Twitter:

    def __init__(self):
        self.following=defaultdict(set)
        self.tweet=defaultdict(list)
        self.time=0


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxHeap=[]
        users= self.following[userId] | {userId}

        for u in users:
            if self.tweet[u]:
                idx=len(self.tweet[u])-1
                t,tid=self.tweet[u][idx]
                heapq.heappush(maxHeap,(-t,tid,idx,u))
        
        while maxHeap and len(res)<10:
            t,tid,idx,u=heapq.heappop(maxHeap)
            res.append(tid)
            if idx-1>=0:
                idx=idx-1
                t,tid=self.tweet[u][idx]
                heapq.heappush(maxHeap,(-t,tid,idx,u))
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