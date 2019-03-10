# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:55:59 2019

@author: Shubham Joshi
This class contains implementation of Binary tree
usage:-
 stack=Stack([4,3,2,6,19,7,9,11,1])
 stack.search_element(8)
 print("get_list")
 stack.get_list() 
 stack.pop()
 stack.peek()
"""

    
from Node import Node
    
class Stack:    
    def __init__(self,elem_lst):
        self.__stack_start__=Node(elem_lst[0])
        
        
        for ele in elem_lst[1:len(elem_lst)]:      
            node=Node(ele)
            node.set_next_node(self.__stack_start__)
            self.__stack_start__=node            
        
            
    def push(self,ele):
        node=Node(ele)
        node.set_next_node(self.__stack_start__)
        self.__stack_start__=node
        
       
    def pop(self):        
        pop_ele=self.__stack_start__.get_dataval()
        self.__stack_start__=self.__stack_start__.get_next_node()
        return pop_ele
     
        
    def peek(self):        
        pop_ele=self.__stack_start__.get_dataval()        
        return pop_ele
    
    def search_element(self,ele):        
        node=self.__stack_start__        
        while(node is not None):            
            if(node.get_dataval()==ele):                 
                return "Found"       
            else:
                node=node.get_next_node()                            
        return "Not Present"
    
    def get_list(self):        
        trav=[]
        node=self.__stack_start__        
        while(node is not None):
            trav.append(node.get_dataval())
            node=node.get_next_node()
        return trav   
   

