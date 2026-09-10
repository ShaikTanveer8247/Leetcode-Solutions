class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        s1_counts=Counter(s1)
        window_counts=Counter(s2[0:k])
        if window_counts==s1_counts:
            return True

        left=0
        right=k-1
        while right<len(s2)-1:
            right+=1
            window_counts[s2[right]]+=1
            window_counts[s2[left]]-=1
            left+=1
            if window_counts==s1_counts:
                return True

        return False
        