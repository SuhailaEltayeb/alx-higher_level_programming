#!/usr/bin/python3
"""Defition of singly linked list classes."""


class Node:
    """node class for singly linked list."""

    def __init__(self, data, next_node=None):
        """New node initialization.
        Arguments:
            data (int): New node data.
            next_node (Node): Next node after new_node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getting and setting new node data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getting and setting next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class of single linked list."""

    def __init__(self):
        """new singly linked list initialization."""
        self.__head = None

    def sorted_insert(self, value):
        """insertion of new node to singly linked list.
        Arguments:
            value (Node): new node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while(tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """function of print formating of singly linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
