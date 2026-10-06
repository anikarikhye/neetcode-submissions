

import collections
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
      
        if endWord not in wordList:
            return 0

        # Build the boxes: pattern -> list of words that match it
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # BFS
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1  # number of words in the sequence so far

        while q:
            # Process everything currently in the queue (one full level)
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            # Finished one level, so the sequence is one word longer
            res += 1

        return 0


