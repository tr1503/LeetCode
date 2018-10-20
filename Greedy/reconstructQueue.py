#Use the greedy and make this algorithm to in-place. 
#Time is O(nlogn), space is O(1).
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #h descend, k ascend
        def myKey(p):
            return -p[0],p[1]
        people.sort(key = myKey)
        for i in range(len(people)):
            if i >= len(people):
                break
            if people[i][1] == i:
                continue
            #insert each pair to its k value's index
            temp = people[i]
            people.pop(i)
            people.insert(temp[1],temp)
        return people
