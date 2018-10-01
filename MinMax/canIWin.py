class Solution(object): 
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def win(M, T, m, state):
            #The other player already win, so T is smaller or equal to 0
            if T <= 0: 
                return False
            #The repeated situation, check the result at m
            if m[state] != 0:
                return m[state] == 1
            for i in range(M):
                #number i used
                if (state & (1 << i)) > 0:
                    continue
                #The other player can't win, so you win
                if not win(M, T-i-1, m, state | (1 << i)):
                    m[state] = 1
                    return True
            #At the end, you can't win
            m[state] = -1
            return False
        
        #The sum of all numbers < target value, no one can win
        if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
            return False
        #This player win
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 == desiredTotal:
            return maxChoosableInteger % 2 == 1
        m = [0] * (1 << maxChoosableInteger) #0 for unknown, 1 for win, -1 for lose
        return win(maxChoosableInteger, desiredTotal, m, 0)
