'''Set a dictionary with dict[key] = []. The list includes all anagrams with same characters.
Use sorted() to get what characters they have. Use list to get all values in dict based on the key.'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for s in strs:
            dic["".join(sorted(s))] += [s]
        return list(dic.values())
