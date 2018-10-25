class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #Stack way: Time O(n), space O(n)
        stack1 = []
        stack2 = []
        for c in S:
            if len(stack1) != 0 and c == '#':
                stack1.pop()
            if c != '#':
                stack1.append(c)
        for c in T:
            if len(stack2) != 0 and c == '#':
                stack2.pop()
            if c != '#':
                stack2.append(c)
        return str(stack1) == str(stack2)
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
        
        # Other way for two points with O(n) time and O(1) space
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in itertools.izip_longest(F(S),F(T)))
