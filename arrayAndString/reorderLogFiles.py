class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        nums = []
        for log in logs:
            logSplit = log.split(" ")
            if logSplit[1].isalpha():
                letters.append((" ".join(logSplit[1:]), logSplit[0]))
            else:
                nums.append(log)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums
