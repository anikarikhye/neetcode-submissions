'''
We will have a general hashmap in which we will have the userid as the key and the value as a list in which we will store the tweetIds. We will have an additional list in the value where we will have time stamps. now how exactly do we know the time stamp for each tweetId remains a question

Now for each user's specific feed, we also need to take into account the followees that the user is following.
For this we will have to make a new "feed" dictionary in which we will have the key as the user herself and the value as a list of all those the user follows.
While the "getNewsFeed" function is getting implemented, we will go to the "feed" dictionary , go search the userid in the list of keys and then in the list we will get all the participants of the feed and for each user in the list we will go to the general dictionary to get the tweetIds


'''
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.general = defaultdict(list) 
        self.feed = defaultdict(set)      
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.general[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        all_users = set(self.feed[userId])
        all_users.add(userId)
        all_tweets = []
        for u in all_users:
            if u in self.general:
                all_tweets.extend(self.general[u])
        
        
        all_tweets.sort(key=lambda x: x[0], reverse=True)
        
       
        return [tweet_id for timestamp, tweet_id in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.feed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.feed[followerId]:
            self.feed[followerId].remove(followeeId)
