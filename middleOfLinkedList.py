# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
class LinkedListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    
    def count(node, val):
        current = node
        count = 1
        while node.next != None:
            current = node.next
            count+=1
        return count
    
    def middleNode(count, node):
        pass