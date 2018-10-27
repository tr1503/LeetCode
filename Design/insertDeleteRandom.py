class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomSet:
            return False
        self.arr.append(val)
        self.randomSet[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomSet:
            return False
        index = self.randomSet[val]
        last = self.arr[-1]
        self.arr[-1] = self.arr[index]
        self.arr[index] = last
        self.randomSet[last] = index
        self.arr.pop()
        self.randomSet.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
