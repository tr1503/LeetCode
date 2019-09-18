class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = index = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            if count == 0:
                index = i
                count = 1
            else:
                rnd = random.randint(0, count)
                if rnd == count:
                    index = i
                count += 1
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
