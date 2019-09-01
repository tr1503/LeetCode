class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = ""
        vals = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                s = mul + vals[p2]
                vals[p1] += s // 10
                vals[p2] = s % 10
        for val in vals:
            if not res and val == 0:
                continue
            else:
                res += str(val)
        return "0" if not res else res
