class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        i = 0
        ans = ""
        while i < len(num1) or i < len(num2):
            val = 0
            if i < len(num1):
                val += int(num1[i])
            if i < len(num2):
                val += int(num2[i])
            ans += str((val+carry) % 10)
            carry = int((val+carry) / 10)
            i+=1
            
        if carry > 0:
            ans += '1'
        ans = ans[::-1]
        return ans
