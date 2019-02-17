#Test code to treap.py
from treap import *

def test():
    """test code to treap.py"""
    treap = Treap()
    treap.add("A", 2)
    treap.add("B", 123)
    treap.add("C", 23)
    treap.add("D", "T")
    all = treap.get_all()
    assert treap.size() == 4
    assert treap.search("A") == all[0]
    assert treap.get_min() == all[0]
    assert treap.get_max() == all[3]
    assert treap.size() == 4
    assert treap.remove("A") is True
    assert treap.size() == 3
    assert treap.remove("C") is True
    assert treap.size() == 2
    assert treap.get_min() == all[1]
    assert treap.get_max() == all[3]
    assert treap.search("B") == all[1]
    assert all[0].key == "A"
    assert all[1].key == "B"
    assert all[2].key == "C"
    assert all[3].key == "D"
    assert all[0].value == 2
    assert all[1].value == 123
    assert all[2].value == 23
    assert all[3].value == "T"
    assert treap.add("F", 0) is True
    all_plus = treap.get_all()
    assert treap.get_max() == all_plus[4]
    assert treap.size() == 5
    assert treap.clear() is True
    assert treap.size() == 0
    assert treap.get_root() is None
    assert treap.add("A", 5) is True
    assert treap.get_root() == all[0]
    assert treap.size() == 1
    assert treap.remove("A") is True
    assert treap.size() == 0
    assert treap.get_root() is None



if __name__ == '__main__':
    test()
