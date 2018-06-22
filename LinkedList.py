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
			print("LinkedList empty !")
		else:
			curr = self.head
			print("\nThe LinkedList:")
			while curr:
				print("{} -> ".format(curr.data), end = "")
				curr = curr.next
			print("None\n")


	def search(self, data):
		if self.head == None:
			print("LinkedList empty !")
		else:
			flag = 0
			curr = self.head
			while curr:
				if data == curr.data:
					flag = 1
					print("Element Found !")
					break
				curr = curr.next
			if flag == 0:
				print("Element not found !")


