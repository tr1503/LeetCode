# The detail is at https://blog.csdn.net/fuxuemingzhu/article/details/82947707
# time is O(n), space is O(n)
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0]
        left = [0] * n
        right = [n - k] * n
        mx = 0
        res = [0, 0, 0]
        for i, num in enumerate(nums):
            sums.append(sums[-1] + num)
        total = sums[k] - sums[0]
        for i in range(k, n):
            if sums[i + 1] - sums[i - k + 1] > total:
                left[i] = i - k + 1
                total = sums[i + 1] - sums[i - k + 1]
            else:
                left[i] = left[i - 1]
        total = sums[n] - sums[n - k]
        for j in range(n - k - 1, -1, -1):
            if sums[j + k] - sums[j] >= total:
                right[j] = j
                total = sums[j + k] - sums[j]
            else:
                right[j] = right[j + 1]
        for i in range(k, n - 2 * k + 1):
            l, r = left[i - 1], right[i + k]
            total = (sums[i + k] - sums[i]) + (sums[l + k] - sums[l]) + (sums[r + k] - sums[r])
            if total > mx:
                mx = max(mx, total)
                res = [l, i, r]
        return res
