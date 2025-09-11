#https://leetcode.com/problems/reverse-linked-list-ii/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head,left,right):
        if left==right:
            return head
        
        dummy = ListNode(0, head) 
        temp= dummy
        prev=None

        for _ in range(left-1):
            temp=temp.next

        curr=temp.next
        oldhead=curr

        for _ in range (right-left+1):
            newnode=curr.next
            curr.next=prev
            prev=curr
            curr=newnode

        temp.next=prev

        oldhead.next=curr

        return dummy.next