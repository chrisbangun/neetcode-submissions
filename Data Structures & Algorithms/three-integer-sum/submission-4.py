"""
Thought process:
Given an integer array, we need to find 3 numbers a, b and c such that a + b + c = 0. 
We can then rewrite this formula as b + c = -a
Now, let's try to sort the array and see if this helps:
- Original input: [-1, 0, 1, 2, -1, -4]
- Sorted input: [-4, -1, -1, 0, 1, 2]

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
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans