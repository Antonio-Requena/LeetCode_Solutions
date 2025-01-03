class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        nSplit = 0
        sumLeft = 0
        sumRight = sum(nums)
        N = len(nums)
        for i in range(N - 1):
            # Update sum first i + 1 & last n - i - 1 elements
            sumLeft += nums[i]
            sumRight -= nums[i]
            if sumRight <= sumLeft and i < N - 1:
                nSplit += 1
