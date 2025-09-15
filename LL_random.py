#https://leetcode.com/problems/linked-list-random-node/

import random
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution(object):

    def __init__(self, head):
        self.head=head
        self.length=0
        curr=head
        while curr:
            self.length+=1
            curr=curr.next

    def getRandom(self):
        x=random.randint(0,self.length-1)
        curr=self.head
        while x>0:
            curr=curr.next
            x-=1
        return curr.val