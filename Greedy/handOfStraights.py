# use greedy algorithm to sort the array firstly and get the first straight.
# delete first straight's number by using a visited array
# time is O(nlogn)
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W != 0:
            return False
        # sort the array firstly
        hand.sort()
        visited = [False for _ in range(n)]
        for i in range(n):
            if visited[i] == False:
                count = 1
                pre = hand[i]
                j = i + 1
                visited[i] = True
                while count < W:
                    if j >= n:
                        break
                    if pre + 1 == hand[j] and visited[j] == False:
                        visited[j] = True
                        count += 1
                        pre = hand[j]
                        j += 1
                    else:
                        j += 1
                if count != W:
                    return False
        return True
