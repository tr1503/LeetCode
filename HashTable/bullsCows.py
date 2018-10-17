class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        nums = [0 for _ in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                nums[int(secret[i])] += 1
                if nums[int(secret[i])] <= 0:
                    B += 1
                nums[int(guess[i])] -= 1
                if nums[int(guess[i])] >= 0:
                    B += 1
        return str(A) + "A" + str(B) + "B"
