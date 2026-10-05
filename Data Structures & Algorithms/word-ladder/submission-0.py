from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])  # (word, number of words in sequence so far)
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            # Try changing each position to every letter a-z
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in words and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))

        return 0

        