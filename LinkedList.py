# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:55:59 2019

@author: Shubham Joshi
This class contains implementation of Binary tree
usage:-
 llist=LinkedList([4,3,2,6,19,7,9,11,1])
 llist.search_element(8)
 print("get_list")
 llist.get_list() 
"""

from Node import Node
    
class LinkedList:    
    def __init__(self,elem_lst):
        self.__llist_start__=Node(elem_lst[0])
        self.__llist_end__=self.__llist_start__
        
        for ele in elem_lst[1:len(elem_lst)]:      
            node=Node(ele)
            self.__llist_end__.set_next_node(node)
            self.__llist_end__=node            
        
            
    def add_element(self,ele):
        node=Node(ele)
        self.__llist_end__.set_next_node(node)
        self.__llist_end__=node
        
        
    def search_element(self,ele):        
        node=self.__llist_start__        
        while(node is not None):            
            if(node.get_dataval()==ele):                 
                return "Found"       
            else:
                node=node.get_next_node()                            
        return "Not Present"
    
    def get_list(self):        
        trav=[]
        node=self.__llist_start__        
        while(node is not None):
            trav.append(node.get_dataval())
            node=node.get_next_node()
        return trav   
   

