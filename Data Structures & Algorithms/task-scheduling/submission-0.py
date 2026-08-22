'''
Steps
Step-1: We start with any character(x) and then create a for loop for n times in which we create an array in which all characters that are not x are added and then add them to the result list and we repeat this process recursively, adding blank space wherever the array for available characters is empty
Step-2: We then return the length of the result array
'''
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_freq)
        formula_length = (max_freq - 1) * (n + 1) + num_max
        return max(formula_length, len(tasks))