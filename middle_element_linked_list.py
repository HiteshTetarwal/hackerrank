# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def length(self,data):
        curr=data
        total=1
        while curr.next!=None:
            total=total+1
            curr=curr.next
        return total

    def middleNode(self, head: ListNode) -> ListNode:
        size=self.length(head)
        last,half=head,head
        if size==2:
            return half.next
        if size%2 != 0:
            while last.next != None:
                last=last.next.next
                half=half.next
            return half
        else:
            i=1
            while True:
                half=half.next
                i=i+1
                if size/i==2:
                    half=half.next
                    break
            return half