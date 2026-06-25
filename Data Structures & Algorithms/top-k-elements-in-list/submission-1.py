# build freq count
# build min heap
import heapq
from collections import defaultdict
class Solution:
    def get_freq_count(self, nums: List[int]) -> Dict[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = self.get_freq_count(nums)
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]