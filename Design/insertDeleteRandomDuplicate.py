class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(set)
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            self.dic[val].add(len(self.arr))
            self.arr.append(val)
            return False
        else:
            self.dic[val] = set([len(self.arr)])
            self.arr.append(val)
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        index = self.dic[val].pop()
        if len(self.dic[val]) == 0:
            del self.dic[val]
        if index != len(self.arr) - 1:
            last = self.arr[-1]
            self.dic[last].remove(len(self.arr) - 1)
            self.dic[last].add(index)
            self.arr[index] = last
        self.arr.pop()
        return True
    
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
