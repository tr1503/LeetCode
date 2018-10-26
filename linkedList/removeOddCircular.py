class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None

def removeOddCircular(head):
	if not head:
		return
	if head.next == head:
		return
	curr = head
	dummy = head
	while curr != dummy and curr.next != dummy:
		if curr == head:
			dummy = head
		temp = curr.next
		curr.next = curr.next.next
		del temp
		curr = curr.next
