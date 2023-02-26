import pytest
import types

from generators import LinkedList


# @pytest.mark.skip()
def test_iter_for_in():
    fruits = LinkedList(['apple', 'peach', 'pear'])
    fruits_lst = []
    for fruit in fruits:
        fruits_lst.append(fruit)
    assert fruits_lst == ['apple', 'peach', 'pear']


# @pytest.mark.skip()
def test_iter_empty_lst():
    fruits = LinkedList([])
    assert list(fruits) == []


# @pytest.mark.skip()
def test_iter_single_item():
    fruits = LinkedList(['apple'])
    assert list(fruits) == ['apple']


# @pytest.mark.skip()
def test_iter_return_type():
    fruits = LinkedList(['apple', 'peach', 'pear'])
    assert isinstance(iter(fruits), types.GeneratorType)


# @pytest.mark.skip()
def test_len_():
    fruits = LinkedList(['apple', 'peach', 'pear'])
    assert len(fruits) == 3


# @pytest.mark.skip()
def test_len_empty_lst():
    fruits = LinkedList([])
    assert len(fruits) == 0


# @pytest.mark.skip("pending")
def test_len_large_lst():
    fruits = LinkedList(range(5000))
    assert len(fruits) == 5000
