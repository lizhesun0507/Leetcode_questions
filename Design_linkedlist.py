# -*- coding: utf-8 -*-
###############################################################################
### Design a linked list                                              
### Author： Lizhe Sun      
###############################################################################

###
### Define the class of the node
###
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

###
### Define the class of LinkedList
###
class LinkedList:
    ### Initialize the linked list
    def __init__(self):
        self.head = None

    ### This function is in the linked list.
    ### Add the node at the head
    def add_at_head(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    
    ### This function is in the linked list
    ### Add the node at the end    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    ### This function is in the linked list
    ### Get the value for the given index
    ### If none, return -1
    ### The index start from 0, it means the head is index as 0
    def get_at_index(self, index):
        if index < 0:
            return -1
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        return -1
    
    ### This function is in the linkedlist
    ### Get the size for the linked list
    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    ### This function is in the linked list
    ### add the new node before the current node
    ### if the index is 0, we add the new node as head
    ### if the index is the size of the linked list, we add the new node at the end of the linked list
    def add_at_index(self, index, new_value):
        if index == 0:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            return 
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
            if current is None:
                break
        if current is None:
            print("The index is out of the length of the linked list")
        else:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node
    
    ### This function is in the linked list
    ### Delete the node by index        
    def delete_at_index(self, index):
        if index < 0:
            return 
        if index == 0:
            current = self.head
            self.head = current.next
            current = None
            
        current = self.head
        count = 0
        while count < index - 1 and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        if current.next is None:
            return
        current.next = current.next.next
            

mylinkedlist = LinkedList()

mylinkedlist.add_at_head(2)

mylinkedlist.add_at_head(1)

mylinkedlist.append(4)

mylinkedlist.append(5)

mylinkedlist.add_at_index(2, 3)

mylinkedlist.get_size()

mylinkedlist.get_at_index(0)

mylinkedlist.get_at_index(1)

mylinkedlist.get_at_index(2)

mylinkedlist.get_at_index(3)

mylinkedlist.get_at_index(4)
        
mylinkedlist.delete_at_index(1)           

mylinkedlist.get_at_index(0)        

mylinkedlist.get_at_index(1)            
        
        
        
            
            
    

