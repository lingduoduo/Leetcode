class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number_of_most_recent_tweets = 10
        self.followings = collections.defaultdict(set)
        self.messages = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1
        self.messages[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        max_heap = []
        if self.messages[userId]:
            heapq.heappush(max_heap, (-self.messages[userId][-1][0], userId, 0))

        for uid in self.followings[userId]:
            if self.messages[uid]:
                heapq.heappush(max_heap, (-self.messages[uid][-1][0], uid, 0))

        result = []
        while max_heap and len(result) < self.number_of_most_recent_tweets:
            t, uid, curr = heapq.heappop(max_heap)
            nxt = curr + 1;
            if nxt != len(self.messages[uid]):
                heapq.heappush(max_heap, (-self.messages[uid][-(nxt+1)][0], uid, nxt))
            result.append(self.messages[uid][-(curr+1)][1]);
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.followings[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followings[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)