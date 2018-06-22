class Node():

	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None


	def insert(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(data)
		print("{} added successfully !".format(data))


	def display(self):
		if self.head == None:
			print("Linked List empty !")
		else:
			curr = self.head
			print("\nThe LinkedList:")
			while curr:
				print("{} -> ".format(curr.data), end = "")
				curr = curr.next
			print("None\n")