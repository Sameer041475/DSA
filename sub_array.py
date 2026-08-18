class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        ans = 0

        for i in range(len(nums)):

            # Count current number
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

            # If count is greater than k
            while count[nums[i]] > k:
                count[nums[left]] -= 1
                left += 1

            # Find maximum length
            ans = max(ans, i - left + 1)

        return ans