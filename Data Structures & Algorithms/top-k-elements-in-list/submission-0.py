# build freq count
# build min heap
import heapq
from collections import defaultdict
class Solution:
    def get_freq_count(self, nums: List[int]) -> List[Tuple[int, int]]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return [(count, num) for num, count in counter.items()]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = self.get_freq_count(nums)
        print(heap)
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        return [num for _, num in heap]