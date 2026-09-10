class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[0:k])
        max_sum=window_sum
        left=0
        right=k-1
        while right<len(nums)-1:
            right+=1
            window_sum=window_sum-nums[left]+nums[right]
            left+=1
            if window_sum>max_sum:
                max_sum=window_sum
        return max_sum/k