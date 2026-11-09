'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''


import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)


    def addNum(self, num: int) -> None:
        if num>self.maxheap[0]:
            heapq.heappush(self.minheap,num)
        if num<self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)

        # Balance it out
        if(abs(len(self.maxheap)-len(self.minheap))>=2):
            popped=heapq.pop(max(len(self.maxheap), len(self.minheap)))
            heapq.heappush(min(len(self.maxheap), len(self.minheap)),-popped)
    

    def findMedian(self) -> float:
        if self.maxheap>self.minheap:
            return -self.maxheap[0]
        elif self.minheap>self.maxheap:
            return self.minheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2