class Solution:
    def convertHundred(self, num):
        v1 = ["","One","Two","Three","Four","Five","Six","Seven","Eight",
              "Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen",
              "Sixteen","Seventeen","Eighteen","Nineteen"]
        v2 = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        res = ""
        a = num // 100
        b = num % 100
        c = num % 10
        if b < 20:
            res = v1[b]
        else:
            if c != 0:
                res = v2[b // 10] + " " + v1[c]
            else:
                res = v2[b // 10]
        if a > 0:
            if b != 0:
                res = v1[a] + " Hundred" + " " + res
            else:
                res = v1[a] + " Hundred"
        return res
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = self.convertHundred(num % 1000)
        v = ["Thousand","Million","Billion"]
        for i in range(3):
            num = num // 1000
            if num % 1000 != 0:
                res = self.convertHundred(num % 1000) + " " + v[i] + " " + res
        while res[-1] == " ":
            res = res[:-1]
        return res
