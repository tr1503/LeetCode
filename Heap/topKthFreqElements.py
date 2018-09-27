'''Use the hashmap by counters to get the freq of each number.
Use max heap to sort the key by their counts. And return the first kth values in heap.'''
class Solution(object): 
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.Counter(nums)
        heap = []
        for key, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap,(count,key))
            else:
                if heap[0][0] < count:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(count,key))
        return [x[1] for x in heap]
