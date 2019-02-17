# By: Måns Rasmussen
# Treap - a balanced binary search tree
# Version 1.0
# (This work is licensed under a CC BY 3.0 license)
"""
A treap or a randomized binary search tree that stores items in a sorted order and offers efficient lookup,
addition and removal of items in the treap.

A treap is a combination of a randomly balanced binary search tree where each node contains a key from a well-ordered set and a heap,
a specialized tree-based data structure that satisfies the heap property; "the parent node has a larger key then its children". 
Each node has a key, value and a priority number.

For each node n in the randomized binary search tree (treap) the following invariants hold:
    *Every node in the left subtree of n contains a key which is smaller than the key in the node n.
    *Every node in the right subtree of n contains a key which is larger than the key in the node n.
    *Assigns a random priority number to each node before it being inserted it into the treap.
    *make sure that each node in the treap has higher priority than its children.
    (with higher priority means smaller number. i.e. in priority order (highest first), 1 -> 2 -> 34 etc.)

(OBS! The randomized function is set to give randomized numbers between 0 and sys.maxsize. 
   sys.maxsize is usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.)
"""

import random

MAX_RANDOM = sys.maxsize   #An integer giving the maximum value a variable of type Py_ssize_t can take.
                           

class Node:
    """A node of the treap that can store values"""
    def __init__(self, key, value, right=None, left=None, priority=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.priority = priority
        if self.priority is None:
            self.priority = random.randint(0, MAX_RANDOM)

    def _add(self, new_node):
        """Adds a new node to the treap"""
        if new_node.key < self.key:
            if self.left is None:
                self.left = new_node
            else:
                self.left._add(new_node)
            if self.priority > self.left.priority:
                self._rotate_right()
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right._add(new_node)
            if self.priority > self.right.priority:
                self._rotate_left()

    def _rotate_left(self):
        """rotates the subtree to this specific node using a left rotation"""
        new_child = Node(self.key, self.value, self.right.left, self.left, self.priority)
        self.key = self.right.key
        self.value = self.right.value
        self.priority = self.right.priority
        self.right = self.right.right
        self.left = new_child

    def _rotate_right(self):
        """rotates the subtree to this specific node using a right rotation"""
        new_child = Node(self.key, self.value, self.right, self.left.right, self.priority)
        self.key = self.left.key
        self.value = self.left.value
        self.priority = self.left.priority
        self.left = self.left.left
        self.right = new_child

    def __str__(self):
        return str([self.key, self.value, self.priority])

    def __repr__(self):
        return str([self.key, self.value, self.priority])

class Treap:
    """A treap containing all the following public methods:
        *search(key)       -> returns the node of the given key, returns False if not in the treap.
        *add(key, value)   -> adds a node to the treap, returns True if successful (OBS! The input key can't already exist in the treap or be None.)
        *remove(key)       -> removes the node specified from the treap, returns True if successful
        *get_root()        -> returns the root of the treap (OBS: if treap is empty the root will be None)
        *get_min()         -> returns the minimum (by key) node in the treap
        *get_max()         -> returns the maximum (by key) node in the tree
        *get_all()         -> returns all of the treaps nodes in an array
        *size()            -> returns an interger representing the total number of nodes in the treap
        *clear()           -> removes all node from the tree, returns True if successful
        
        OBS! Be consistent with the keys you use! e.g. if keys are strings, allways use strings as keys.
        """
    
    def __init__(self):
        """Initialize an empty root in the treap"""
        self.__root = None
        self.__size = 0
        self.array = []

    def search(self, key):
        """Runs _search() (which is a recursive function)"""
        return self._search(key, self.__root)

    def _search(self, key, node):
        """Searches for a node in the tree by the key given, returns that node"""
        if node is None:
            return False
        else:
            if key == node.key:
                return node
            elif key < node.key:
                return self._search(key, node.left)
            else:
                return self._search(key, node.right)

    def add(self, key, value):
        """Adds a new node to the treap with the given data.
           Returns True if successful or raises an error if invalid input
           Valid input is key that is not None or already exist in the treap"""
        if key is None:
            raise ValueError("Can't add a node with 'None' as key")
        if self.search(key) is not False:
            if self.search(key).key == key:
                raise ValueError("There is already a node in the treap with this key!")
        new_node = Node(key, value)
        if self.__size == 0:
            self.__root = new_node
        else:
            self.__root._add(new_node)
        self.__size += 1
        return True

    def remove(self, key):
        """Removes the node with the key given from the treap
           Returns True if successful or raises an error if invalid input.
           Invalid input is if key is not in treap or treap is already empty"""
        if self.search(key) is False:
            raise ValueError("This node is not in the treap!")
        elif self.__root is not None:
            self.__root = self._remove(key, self.__root)
            self.__size -= 1
            return True
        else:
            raise ValueError("The treap is already empty!")

    def _remove(self, key, node):
        """Removes the node with the key given from the treap, returns the updated treap"""
        if node is not None:
            if node.key == key:
                if node.left is None and node.right is None:
                    return None
                else:
                    if node.left is None:
                        return node.right
                    elif node.right is None:
                        return node.left
                    else:
                        if node.right.priority > node.left.priority:
                            node._rotate_left()
                            node.left = self._remove(key, node.left)
                        else:
                            node._rotate_right()
                            node.right = self._remove(key, node.right)
            elif key < node.key:
                node.left = self._remove(key, node.left)
            elif key > node.key:
                node.right = self._remove(key, node.right)
        return node

    def get_min(self):
        """Returns the node with the minimum key in the tree
            returns None if treap is empty"""
        node = self.__root
        while node.left is not None:
            node = node.left
        return node

    def get_max(self):
        """Returns the node with the maximum key in the tree
            returns None of treap is empty"""
        node = self.__root
        while node.right is not None:
            node = node.right
        return node

    def get_root(self):
        """returns the root of the tree"""
        return self.__root

    def get_all(self):
        """returns all the nodes in the treap in alphabetical order.
           If the treap is empty returns an empty array"""
        self.array = []
        if self.__root is None:
            return []
        else:
            self.array = self._get_all(self.__root)
            return self.array

    def _get_all(self, node):
        """Goes through all the nodes in the treap and saves the nodes in an array,
           returns that array"""
        if node is None:
            return
        else:
            self._get_all(node.left)
            self.array.append(node)  # saves the nodes in an array
            self._get_all(node.right)
        return self.array

    def size(self):
        """Returns the size of the treap and checks if the size matches the number of nodes in the treap,
            raises valueerror if _count_nodes() and self.__size() doesn't equal"""
        count = self._count_nodes(self.__root)
        if count == self.__size:
            return self.__size
        else:
            raise ValueError("There is something wrong with the treap!")

    def clear(self):
        """Clears the tree from all nodes, returns True"""
        self.__root = None
        return True

    def _count_nodes(self, node):
            """Counts the nodes in the treap"""
            if node is not None:
                counter = 1
                if node.left is not None:
                    counter += self._count_nodes(node.left)
                if node.right is not None:
                    counter += self._count_nodes(node.right)
                return counter
            else:
                return 0
