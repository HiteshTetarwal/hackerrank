class node:
	def  __init__(self,data=None):
		self.data=data
		self.next=None
class linked_list:
	"""docstring for linked_list"""
	def __init__(self):
		self.head = node()

	def append(self,data):
		new_node=node(data)
		curr=self.head
		while curr.next!=None:
			curr=curr.next
		curr.next =new_node

	def length(self):
		curr=self.head
		total=0
		while curr.next!=None:
			total=total+1
			curr=curr.next
		return total

	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def get(self,index):
		if index>=self.length():
			print("Error with index")
		cur_index=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_index==index: return cur_node.data
			cur_index+=1

	def erase(self,index):
		if index>=self.length():
			print("Error with index")
			return
		cur_index=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_index==index:
				last_node.next=cur_node.next
				return
			cur_index+=1

my_list=linked_list()


my_list.append(1)

my_list.append(2)

my_list.append(3)

my_list.append(4)
print("Element at index given",my_list.erase(2),my_list.display())


		




class Solution:
    
    def length(data):
        curr=data
        total=0
        while curr.next!=None:
            total=total+1
            curr=curr.next
        return total

    def middleNode(self, head: ListNode) -> ListNode:
        length=length(head)
        last,half=head,head
        if length%2!=0:
            while last.next != None:
                last=last.next.next
                half=half.next
            return half
        else:
            i=1
            while True:
                half=half.next
                i=i+1
                if length/i==0.5:
                    half=half.next
                    break
            return half