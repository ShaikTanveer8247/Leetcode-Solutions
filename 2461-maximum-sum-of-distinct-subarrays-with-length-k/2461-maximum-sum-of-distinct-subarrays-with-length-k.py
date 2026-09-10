class Solution:
    from collections import Counter
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window_sum=sum(nums[0:k])
        counts=Counter(nums[0:k])
        violation=sum(1 for v in counts.values() if v>=2)
        max_sum=window_sum if violation==0 else 0

        left=0
        right=k-1
        while right<len(nums)-1:
            right+=1
            if counts[nums[right]]==1:
                violation+=1
            counts[nums[right]]+=1
            if counts[nums[left]]==2:
                violation-=1
            counts[nums[left]]-=1   

            window_sum=window_sum-nums[left]+nums[right]
            left+=1
            if violation==0 and window_sum>max_sum:
                max_sum=window_sum
        return max_sum