class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        dic = {}
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split(" ")
        for word in words:
            if word and word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    dic[word] += 1
        return max(dic, key = lambda key : dic[key])
