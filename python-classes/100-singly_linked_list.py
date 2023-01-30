#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 3:08:00 2023.

@author: jgnacio
@description:
This file contains classes for the construction of a single
linked list.
"""


class Node(object):
    """This class represents a node in a linked list."""

    def __init__(self, data, next_node=None):
        """Initialize this node with the given data."""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data stored in this node."""
        return self.__data

    @property
    def next_node(self):
        """Return the next node in the linked list."""
        return self.__next_node

    @data.setter
    def data(self, data):
        """Set the data stored in this node to the given value."""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @next_node.setter
    def next_node(self, value):
        """Set the next node to the given value (other node or None)."""
        if not isinstance(value, Node) or value is None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList(object):
    """This class represents a linked list."""

    def __init__(self):
        """Initialize this linked list with an empty node."""
        self.__head = None

    def __str__(self):
        """Return a string representation of this linked list."""
        if self.__head is None:
            return '[]'
        current = self.__head
        items = []
        while current is not None:
            items.append(str(current.data))
            current = current.next_node
        return '[' + ', '.join(items) + ']'

    def sorted_insert(self, value):
        """Insert the given value at the beginning of this linked list."""
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            current = self.__head
            prev = None
            while current.next_node is not None:
                if current.data < node.data:
                    break
                prev = current
                current = current.next_node
            else:
                print(f"Current: {current.data} c_next: {current.next_node}, Node: {node.data}")
                print(f"Prev: {prev.data} c_next: {prev.next_node}, Node: {node.data}")
                current.next_node = node
            print(f"2Current: {current.data} c_next: {current.next_node.data if isinstance(current, Node) else None}, Node: {node.data}")
