class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #Two pointers: time O(n) space O(1)
        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0
        
        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break
            
            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break
            
            
            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a" 
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False
            
            si -= 1
            ti -= 1
        return True
