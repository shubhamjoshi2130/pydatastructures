# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:55:59 2019

@author: Shubham Joshi
This class contains implementation of Binary tree
usage:-
 queue=Queue([4,3,2,6,19,7,9,11,1])
 queue.search_element(8)
 print("get_list")
 queue.get_list() 
 queue.enqueue(45)
 queue.get_list() 
 queue.dequeue()
 queue.get_list() 
 queue.dequeue()
 queue.get_list() 
"""

from Node import Double_Linked_Node
    
class Queue:    
    def __init__(self,elem_lst):
        self.__queue_start__=Double_Linked_Node(elem_lst[0])
        self.__queue_end__=self.__queue_start__
        
        for ele in elem_lst[1:len(elem_lst)]:  
            node=Double_Linked_Node(ele)            
            node.set_right(self.__queue_start__)
            self.__queue_start__.set_left(node)            
            self.__queue_start__=node
            
    def enqueue(self,ele):
        node=Double_Linked_Node(ele)            
        node.set_right(self.__queue_start__)
        self.__queue_start__.set_left(node)            
        self.__queue_start__=node
     
    def dequeue(self):
        end_node=self.__queue_end__        
        self.__queue_end__=self.__queue_end__.get_left()        
        end_node.get_left().set_right(None)
        end_node.set_left(None)
        end_node.set_right(None)
        return end_node.get_dataval()
        
    def peek(self):
        return self.__queue_end__.set_dataval()
    
    def search_element(self,ele):        
        node=self.__queue_start__        
        while(node is not None):            
            if(node.get_dataval()==ele):                 
                return "Found"       
            else:
                node=node.get_right()                            
        return "Not Present"
    
    def get_list(self):        
        trav=[]
        node=self.__queue_start__        
        while(node is not None):
            trav.append(node.get_dataval())
            node=node.get_right()
        return trav   
   

