#https://leetcode.com/problems/linked-list-cycle-ii/description/

class Solution(object):
    def detectCycle(self, head):
        slow=head
        fast=head
        while fast!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return -1
            