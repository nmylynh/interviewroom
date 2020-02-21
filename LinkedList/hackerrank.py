#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'removeKthLinkedListNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeKthLinkedListNode(head, k):
    # Write your code here
    current = head
    dict = {}
    i = 0
    while current:
        dict[i] = current
        i += 1
        current = current.next
    size = len(dict)
    prevNode = size - k - 1
    nextNode = size - k + 1
    
    if k > size:
        return head
    elif dict.get(nextNode) and dict.get(prevNode):
        dict[prevNode].next = dict[nextNode]
    elif dict.get(prevNode):
        dict[prevNode].next = None
    else:
        head = dict[nextNode]    
    return head


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    k = int(input().strip())

    result = removeKthLinkedListNode(head.head, k)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
