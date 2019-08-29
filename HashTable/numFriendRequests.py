# Use hash table to count each age in the array and compare each age with all possible age by the conditions
# time is O(120 * n), space is O(1)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = collections.Counter(ages)
        ages = sorted(count.keys())
        res = 0
        for A in ages:
            for B in range(int(0.5 * A) + 7 + 1, A + 1):
                res += count[A] * (count[B] - int(A == B))
        return res
