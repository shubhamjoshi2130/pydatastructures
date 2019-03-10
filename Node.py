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