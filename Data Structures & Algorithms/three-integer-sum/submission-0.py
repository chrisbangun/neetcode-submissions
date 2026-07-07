"""
Thought process:
Given an integer array, we need to find 3 numbers a, b and c such that a + b + c = 0. 
We can then rewrite this formula as b + c = -a
Now, let's try to sort the array and see if this helps:
- Original input: [-1, 0, 1, 2, -1, -4]
- Sorted input: [-4, -1, -1, 0, 1, 2]

say:
- a = -4, b = -1, c = 2
- b + c = -a? -1 + 2 = 4? no, 1 > 4, so we move b to the right
- a = -4, b = -1, c = 1, 0 > -4, so we need to move c to the left
- a = -4, b = -1, c = 0, -1 > -4, so we need to move c to the left
- a = -4, b = -1, c = -1, -2 > -4, so we need to move c to the left
- however, b = c is now the same location so we skip and move on to move a to the right

Yeah, I think this algorithm works. What about the Time and Space complexity?
If N is the number of integer in the array, then:
- Time: O(N^2)
- Space: O(N)

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums = sorted(nums)
        ans = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])  # found one valid answer
                    
                    _j = j + 1
                    while nums[j] == nums[_j] and _j < k:
                        _j += 1
                    j = _j
                    
                    _k = k - 1
                    while nums[k] == nums[_k] and j < _k:
                        _k -= 1
                    k = _k                
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
            _i = i + 1
            while _i < len(nums) - 2:
                if nums[_i] == nums[i]:
                    _i += 1
                else:
                    break
            i = _i
                
        return ans