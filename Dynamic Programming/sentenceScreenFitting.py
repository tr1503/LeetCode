class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        '''words = ""
        for word in sentence:
            words += word
            words += " "
        start = 0
        n = len(words)
        for i in range(rows):
            start += cols
            if (words[start % n] == ' '):
                start += 1
            else:
                while start > 0 and words[(start - 1) % n] != ' ':
                    start -= 1
        return start // n'''
        dp = []
        for i in range(len(sentence)):
            count = 0
            j = i
            curr = 0
            while curr < cols:
                curr += len(sentence[j])
                if curr > cols:
                    break
                curr += 1
                count += 1
                j += 1
                if j == len(sentence):
                    j = 0
            dp.append(count)
        index = 0
        res = 0
        for i in range(rows):
            res += dp[index]
            index += dp[index]
            index %= len(sentence)
        return res // len(sentence)
