#!/usr/bin/python3
"""
7. Singly linked list
A class Node that defines a node of a singly linked list
"""


class Node:
    """"Class that defines a node"""

    def __init__(self, data, next_node=None):
        """Define private instance attributes: data & next_node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Function that returns data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Define private instance attribute: value
        Raise TypeError if value is not an integer
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """Define private instance attribute: next_node"""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Define private instance attribute: value
        Raise TypeError if value is not an integer or None/NULL
        """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Define private instance attribute: head(first node)"""

        self.head = None

    def __str__(self):
        """Define private instance attributes: printall & location"""

        printall = ""
        location = self.head
        while location:
            printall += str(location.data) + "\n"
            location = location.next_node

        return printall[:-1]

    def sorted_insert(self, value):
        """Function that inserts new node into correct sorted position"""

        tmp_node = Node(value)
        if not self.head:
            self.head = tmp_node
            return

        if value < self.head.data:
            tmp_node.next_node = self.head
            self.head = tmp_node
            return

        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node

        if location.next_node:
            tmp_node.next_node = location.next_node

        location.next_node = tmp_node
