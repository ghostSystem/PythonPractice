class Node():

	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree():

	def __init__(self):
		self.root = None


	def insert(self, data=None):
		if self.root == None:
			self.root = Node(data)
		else:
			self._insert(self.root, data)


	def _insert(self, curr_node, data):
		if data < curr_node.data:
			if curr_node.left == None:
				curr_node.left = Node(data)
				print("Element added successfully !")
			else:
				self._insert(curr_node.left, data)
		elif data > curr_node.data:
			if curr_node.right == None:
				curr_node.right = Node(data)
				print("Element added successfully !")
			else:
				self._insert(curr_node.right, data)
		else:
			print("Element already in BinaryTree")


	def display(self):
		if self.root == None:
			print("BinaryTree is empty !")
		else:
			self._display(self.root)


	def _display(self, curr_node):
		if curr_node != None:
			self._display(curr_node.left)
			print(curr_node.data)
			self._display(curr_node.right)


	def search(self, data):
		if self.root == None:
			print("BinaryTree is empty !")
		else:
			if self._search(self.root, data):
				print("Element Found !")
			else:
				print("Element Not Found !")


	def _search(self, curr_node, data):
		if data == curr_node.data:
			return True
		elif data < curr_node.data and curr_node.left:
			return self._search(curr_node.left, data)
		elif data > curr_node.data and curr_node.right:
			return self._search(curr_node.right, data)
		return False





