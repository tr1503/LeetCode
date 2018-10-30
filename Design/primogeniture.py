from collections import *
class PersonNode:
    def __init__(self):
        self.children = OrderedDict()
        self.status = True    # True means alive; False means dead
class FamilyTree():
    def __init__(self, ancestors):
        self.root = PersonNode()
        self.family = {}
        for name, status in ancestors:
            if name not in self.root.children:
                childNode = PersonNode()
                childNode.status = status
                self.root.children[name] = childNode
                self.family[name] = childNode

    def birth(self, parent, child):
        if parent not in self.family:
            raise ValueError('This person does not exist in this family!')
        childNode = PersonNode()
        self.family[parent].children[child] = childNode
        self.family[child] = childNode

    def death(self, person):-google 1point3acres
        if person not in self.family:
            raise ValueError('This person does not exist in this family!')
        self.family[person].status = False

    def getOrderOfSuccession(self):
        queue = deque().
        for child in self.root.children:
            childNode = self.root.children[child]
            if childNode.status:-google 1point3acres
                return child
            queue.append(childNode)

        while queue:
            cur = queue.popleft()
            for child in cur.children:
                childNode = cur.children[child]
                if childNode.status:
                    return child
                queue.append(childNode)
