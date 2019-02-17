
# Treap - A randomized binary search tree
A treap or a randomized binary search tree that stores items in a sorted order and offers efficient lookup, addition and removal of items in the treap.

A treap is a combination of a randomly balanced binary search tree where each node contains a key from a well-ordered set and a heap, a specialized tree-based data structure that satisfies the heap property; "the parent node has a larger key then its children".
Each node has a key, value and a priority number. 

For each node n in the treap the following invariants hold:
* Every node in the left subtree of n contains a key which is smaller than the key in the node n.
* Every node in the right subtree of n contains a key which is larger than the key in the node n.
* Assigns a random priority number to each node before it being inserted it into the treap.
* make sure that each node in the treap has higher priority than its children.
(with higher priority means smaller number. i.e. in priority order (highest first), 1 -> 2 -> 34 etc.)

If you want to read more you can read at the [treap wikipedia page](https://en.wikipedia.org/wiki/Treap) or on [yourbasic website](https://yourbasic.org/algorithms/treap/)

### Time complexity
Compared to other data structures the treap is a efficient way to get the best of both worlds so to speak when it comes to have overall good time complexity. Following table shows the averege time complexity for different data structures.

|    Data structure    | Insert | Find | Min/max | Delete |
| ------------------   |:------:|:----:|:-------:|:------:|
| Unsorted array       |       1|     n|        n|       n|
| sorted array         |       1| log n|        n|   log n|
| Unsorted linked list |       1|     n|        n|       n|
| Sorted linked list   |       n|     n|        1|       n|
| Hash table           |       1|     1|        n|       1|
| Treap                |   log n| log n|    log n|   log n|


### Documentation
The treap consists of 2 classes, Node and Treap with the following public methods/functions: 

* search(key)       -> returns the node of the given key, returns False if not in the treap. 
* add(key, value)   -> adds a node to the treap, returns True if successful  (OBS! The input key can't already exist in the treap or be None.)
* remove(key)       -> removes the node specified from the treap, returns True if successful
* get_root()        -> returns the root of the treap (OBS: if treap is empty the root will be None)
* get_min()         -> returns the minimum (by key) node in the treap
* get_max()         -> returns the maximum (by key) node in the tree
* get_all()         -> returns all of the treaps nodes in an array
* size()            -> returns an interger representing the total number of nodes in the treap
* clear()           -> removes all node from the tree, returns True if successful

(OBS! The randomized function is set to give randomized numbers between 0 and 1000 as default. If you want to add more nodes then 1000 you need to increase this upper limit of 1000 (named RAND_MAX) first)

_Version 1.0_
_(Version numbers adhere to [semantic versioning](https://semver.org/))_

*By Måns Rasmussen*

This work is licensed under a [CC BY 3.0 license](https://creativecommons.org/licenses/by/3.0/)
Last eddited: 20 May 2018
