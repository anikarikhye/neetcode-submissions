class MedianFinder:

    def __init__(self):
        self.listt = []

    def addNum(self, num: int) -> None:
        self.listt.append(num)

    def findMedian(self) -> float:
        self.listt.sort()  
        n = len(self.listt)
        mid = n // 2
        if n % 2 == 1:
            return float(self.listt[mid])
        else:
            return (self.listt[mid - 1] + self.listt[mid]) / 2.0
        