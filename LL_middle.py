#https://leetcode.com/problems/middle-of-the-linked-list/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        
        s=(n//2) + 1

        temp = head
        for _ in range(s-1): 
            temp=temp.next
        
        return temp