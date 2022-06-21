from os import pread


class Node:
	def __init__(self,data:str):
		self.data = data
		self.next = None

class LinkedList:
	# def __init__(self):
	# 	self.head = None
	def __init__(self,nodes=None):
		self.head = None
		if nodes is not None:
			node = Node(data=nodes.pop(0))
			self.head = node
			for item in nodes:
				node.next = Node(data=item)
				node = node.next

	def __repr__(self):
		node = self.head
		nodes_list = []
		while node is not None:
			nodes_list.append(f'{node.data}')
			node = node.next
		nodes_list.append("None")
		return " -> ".join(nodes_list)

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def insert_at_start(self,node):
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	

	def insert_at_end(self,node):
		if self.head == None:
			self.head = node
			return
		for current_node in self:
			# print(type(current_node))
			pass
		current_node.next = node
	
	def add_after_node(self,target,new_node):
		if self.head is None:
			raise Exception("List is empty!")
		for node in self:
			if node.data == target:
				new_node.next = node.next
				node.next = new_node
				return
		raise Exception(f"Node with data {target} not found.")
	
	def add_before_node(self,target,new_node):
		if self.head is None:
			raise Exception("List is empty")
		if self.head.data == target:
			return self.insert_at_start(new_node)

		prev_node = self.head
		for node in self:
			if node.data == target:
				prev_node.next = new_node
				new_node.next = node
				return
			prev_node = node
	
	def remove_node(self,target):
		if self.head is None:
			raise Exception("List is empty")
		if self.head.data == target:
			self.head = self.head.next
			return

		prev_node = self.head
		for node in self:
			if node.data == target:
				prev_node.next = node.next
				return
			prev_node = node

		raise Exception(f"Node with data {target} not found!")


if __name__ == "__main__":
	# llist = LinkedList()
	# first_node = Node('a')
	# llist.head = first_node
	# second_node = Node('b')
	# third_node = Node('c')
	# first_node.next = second_node
	# second_node.next = third_node
	llist = LinkedList([1,2,3,4,5,6])
	# print(llist)
	# for node in llist:
	# 	print(node.data,end=' ')
	# print()
	# new_node = Node(7)
	# llist.insert_at_end(new_node)
	# print(llist)
	# llist.add_after_node(12,Node(11))
	# print(llist)
	llist.add_before_node(3,Node(3.4))
	print(llist)
	llist.remove_node(3.4)
	print(llist)