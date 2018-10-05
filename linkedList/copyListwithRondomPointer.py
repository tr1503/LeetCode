# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        ptr = head
        while ptr:
            #Insert clone node between each original node
            #Linked list will become A->A'->B->B'->C->C'
            node = RandomListNode(ptr.label)
            node.next = ptr.next
            ptr.next = node
            ptr = node.next
        ptr = head
        while ptr:
            # Now link the random pointers of the new nodes created.
            # Iterate the newly created list and use the original nodes random pointers,
            # to assign references to random pointers for cloned nodes.
            if ptr.random:
                ptr.next.random = ptr.random.next
            else:
                ptr.next.random = None
            ptr = ptr.next.next
        
        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        old = head
        new = head.next
        old_head = head.next
        while old:
            old.next = old.next.next
            if new.next:
                new.next = new.next.next
            else:
                new.next = None
            old = old.next
            new = new.next
        return old_head
