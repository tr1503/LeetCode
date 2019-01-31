class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = {}
        n = len(nums)
        visited = [False for _ in range(n)]
        for i in range(n):
            if visited[i]:
                continue
            curr = i
            while True:
                visited[curr] = True
                p = (curr + nums[curr]) % n
                if p < 0:
                    p += n
                if p == curr or nums[p] * nums[curr] < 0:
                    break
                if p in m:
                    return True
                m[curr] = p
                curr = p
        return False
