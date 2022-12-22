import pytest

##### Imports

def test_imports():
    import projet3

##### DictChainingLinkedList

def test_dict_chaining_linkedlist_is_empty():
    from projet3 import DictChainingLinkedList
    assert len(DictChainingLinkedList(1)) == 0

def test_dict_chaining_linkedlist_size_is_correct_after_insert():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', 'von Neumann')
    assert len(d) == 1

def test_dict_chaining_linkedlist_size_is_correct_after_replace():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', '?')
    d.insert('John', 'von Neumann')
    assert len(d) == 1

def test_dict_chaining_linkedlist_search():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', 'von Neumann')
    assert d['John'] == 'von Neumann'

def test_dict_chaining_linkedlist_search_after_replace():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', 'von neuman')
    d.insert('John', 'von Neumann')
    assert d['John'] == 'von Neumann'

def test_dict_chaining_linkedlist_search_raises_KeyError():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', 'von Neumann')
    with pytest.raises(KeyError):
        d.search('Alan')

def test_dict_chaining_linkedlist_insert_same_hash():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('a', 'a')
    d.insert('A', 'A')
    assert len(d) == 2

def test_dict_chaining_linkedlist_delete():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('John', 'von Neumann')
    d.delete('John')
    assert len(d) == 0

def test_dict_chaining_linkedlist_delete_raises_KeyError():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    with pytest.raises(KeyError):
        d.delete('John')

def test_dict_chaining_linkedlist_delete_same_hash():
    from projet3 import DictChainingLinkedList
    d = DictChainingLinkedList(16)
    d.insert('a', 'a')
    d.insert('A', 'A')
    d.delete('a')
    assert len(d) == 1

##### DictChainingSkipList

def test_dict_chaining_skiplist_is_empty():
    from projet3 import DictChainingSkipList
    assert len(DictChainingSkipList(1)) == 0

def test_dict_chaining_skiplist_size_is_correct_after_insert():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', 'von Neumann')
    assert len(d) == 1

def test_dict_chaining_skiplist_size_is_correct_after_replace():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', '?')
    d.insert('John', 'von Neumann')
    assert len(d) == 1

def test_dict_chaining_skiplist_search():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', 'von Neumann')
    assert d['John'] == 'von Neumann'

def test_dict_chaining_skiplist_search_after_replace():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', 'O\'Neil')
    d.insert('John', 'von Neumann')
    assert d['John'] == 'von Neumann'

def test_dict_chaining_skiplist_search_raises_KeyError():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', 'von Neumann')
    with pytest.raises(KeyError):
        d.search('Alan')

def test_dict_chaining_skiplist_insert_same_hash():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('a', 'a')
    d.insert('A', 'A')
    assert len(d) == 2

def test_dict_chaining_skiplist_delete():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('John', 'von Neumann')
    d.delete('John')
    assert len(d) == 0

def test_dict_chaining_skiplist_delete_raises_KeyError():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    with pytest.raises(KeyError):
        d.delete('John')

def test_dict_chaining_skiplist_delete_same_hash():
    from projet3 import DictChainingSkipList
    d = DictChainingSkipList(16)
    d.insert('a', 'a')
    d.insert('A', 'A')
    d.delete('a')
    assert len(d) == 1

##### DictOpenAddressing

def test_dict_double_is_empty():
    from projet3 import DictOpenAddressing
    assert len(DictOpenAddressing(1)) == 0

def test_dict_double_size_is_correct_after_insert():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] = 'Turing'
    assert len(d) == 1

def test_dict_double_size_is_correct_after_replace():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] =  '?'
    d['Alan'] = 'Turing'
    assert len(d) == 1

def test_dict_double_search():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] = 'Turing'
    assert d['Alan'] == 'Turing'

def test_dict_double_search_after_replace():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] = '?'
    d['Alan'] = 'Turing'
    assert d['Alan'] == 'Turing'

def test_dict_double_search_raises_KeyError():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] = 'Turing'
    with pytest.raises(KeyError):
        d.search('John')

def test_dict_double_insert_same_hash():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['a'] = 'a'
    d['A'] = 'A'
    assert len(d) == 2

def test_dict_double_delete():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['Alan'] = 'Turing'
    del d['Alan']
    assert len(d) == 0

def test_dict_double_delete_raises_KeyError():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    with pytest.raises(KeyError):
        d.delete('Alan')

def test_dict_double_delete_same_hash():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d['a'] = 'a'
    d['A'] = 'A'
    d.delete('a')
    assert len(d) == 1

def test_dict_double_delete_reorganises_container():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(16)
    d.insert('a', 'a')
    d.insert('A', 'A')
    d.delete('a')
    assert d['A'] == 'A'

def test_dict_double_insert_raises_OverflowError():
    from projet3 import DictOpenAddressing
    d = DictOpenAddressing(1)
    d['John'] = 'von Neumann'
    with pytest.raises(OverflowError):
        d['Alan'] = 'Turing'
