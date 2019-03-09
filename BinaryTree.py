# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:55:59 2019

@author: owner
"""

class Node:
    def __init__(self, dataval=None):
        self.__dataval__ = dataval
        self.__right__ = None
        self.__left__ = None
    
    def get_right(self):
        return self.__right__
    
    def get_left(self):
        return self.__left__
    
    def set_right(self,right):
        self.__right__=right
    
    def set_left(self,left):
        self.__left__=left
    
    def get_dataval(self):
        return self.__dataval__

    def set_dataval(self,dataval):
        self.__dataval__=dataval
    
class BinaryTree:    
    def __init__(self,elem_lst):
        self.__btree_start__=Node(elem_lst[0])
        
        for ele in elem_lst[1:len(elem_lst)]:            
            leaf=self.__btree_start__
            leaf_node=None
            while(leaf is not None):                                
                if(leaf.get_dataval()<ele):                                        
                    leaf_node=leaf
                    leaf=leaf.get_right()
                elif(leaf.get_dataval()>ele):
                    leaf_node=leaf
                    leaf=leaf.get_left()            
            node=Node(ele)
            if(ele>leaf_node.get_dataval()):
                leaf_node.set_right(node)
            elif(ele<leaf_node.get_dataval()):
                leaf_node.set_left(node)
                
    def search_element(self,ele):        
        leaf=self.__btree_start__        
        while(leaf is not None):            
            if(leaf.get_dataval()<ele):                    
                    leaf=leaf.get_right()
            elif(leaf.get_dataval()>ele):                    
                    leaf=leaf.get_left()
            elif(leaf.get_dataval()==ele): 
                    return "Found"                                   
        return "Not Present"
    
    def print_inorder(self):        
        def traverse(node):
            if(node.get_left() is not None):
                traverse(node.get_left())
                            
            print(node.get_dataval())    
            
            if(node.get_right() is not None):
                traverse(node.get_right())
            
        traverse(self.__btree_start__)
        
    def print_postorder(self):        
        def traverse(node):            
            
            if(node.get_left() is not None):
                traverse(node.get_left())
                        
            if(node.get_right() is not None):
                traverse(node.get_right())
            
            print(node.get_dataval())
            
        traverse(self.__btree_start__)
 
    def print_preorder(self):        
        def traverse(node):
            
            print(node.get_dataval())
            
            if(node.get_left() is not None):
                traverse(node.get_left())
                         
            if(node.get_right() is not None):
                traverse(node.get_right())
            
        traverse(self.__btree_start__)
        
btree=BinaryTree([4,3,2,6,19,7,9,11,1])
btree.search_element(8)
print("inorder")
btree.print_inorder()
print("preorder")
btree.print_preorder()
print("postorder")
btree.print_postorder()