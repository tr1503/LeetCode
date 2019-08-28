# Use two points to compare the end of A and the start of B together and the start of A and the end of B together
# If they have intersection, get the max of starts and the min of ends
# time is O(n), space is O(1)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif B[j][1] < A[i][0]:
                j += 1
            else:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    j += 1
        return ans
