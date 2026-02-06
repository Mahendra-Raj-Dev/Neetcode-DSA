# Problem: Design Twitter
# Pattern: heap + hashmap (design)
# Approach:
# - Store tweets with timestamps for each user
# - Use a max-heap to retrieve the 10 most recent tweets from followed users
# - Maintain follow relationships using a hashmap with sets
# Time complexity: 
# - postTweet: O(1)
# - getNewsFeed: O(N log N) in worst case
# - follow/unfollow: O(1)
# Space complexity: O(N)

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId])-1
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
