# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 07:57:05 2019

@author: owner
"""

class Node:
    def __init__(self, dataval=None):
        self.__dataval__ = dataval
        self.__next_node__ = None    
    
    def get_next_node(self):
        return self.__next_node__
        
    def set_next_node(self,next_node):
        self.__next_node__=next_node
    
    def set_dataval(self,dataval):
        self.__dataval__=dataval
        
    def get_dataval(self):
        return self.__dataval__
    

    
class Double_Linked_Node:
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
        
