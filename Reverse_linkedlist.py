# -*- coding: utf-8 -*-
###############################################################################
### Reverse a linked list                                              
### Author： Lizhe Sun      
###############################################################################
from LinkedList import LinkedList
###
### The leetcode solution
### The input is a node, the head
###
class Solution:
    def reverse_linkedlist(self, head):
        ### Define the current
        current = None
        while head:
            temp = head.next
            head.next = current
            current = head
            head = temp
        return current

###
### If the input is a linked list
###
def reverse_linkedlist_v2(input_linkedlist):
    if input_linkedlist.head is None:
        return None
    
    current = input_linkedlist.head
    ### define a head, the value is None
    head = None
    while current:
        temp = current.next
        current.next = head
        head = current
        current = temp
    input_linkedlist.head = head
    return input_linkedlist

###########################################
### Test case
### Define a linkedlist, named mylinkedlist
###########################################
mylinkedlist = LinkedList()
###
### Add values into mylinkedlist
###
mylinkedlist.add_at_head(1)
mylinkedlist.append(2)
mylinkedlist.append(3)
mylinkedlist.append(4)
mylinkedlist.append(5)

### Test the length of the linkedlist
assert(mylinkedlist.get_size() == 5)

### Reverse the linkedlist
reverse_linkedlist = reverse_linkedlist_v2(mylinkedlist)

### Get the value for linkedlist
assert(reverse_linkedlist.get_at_index(0) == 5)
assert(reverse_linkedlist.get_at_index(1) == 4)
assert(reverse_linkedlist.get_at_index(2) == 3)
assert(reverse_linkedlist.get_at_index(3) == 2)
assert(reverse_linkedlist.get_at_index(4) == 1)
    