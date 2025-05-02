"""Unit tests for the Sorting assignment."""

__author__ = 'Alain Kägi'
 
import my_selection
import random

def test_empty():
    a = []
    my_selection.sort(a)
    assert a == []

def test_singleton():
    a = [0]
    my_selection.sort(a)
    assert a == [0]

def test_worst_case():
    a = [5, 4, 3, 2, 1, 0]
    my_selection.sort(a)
    assert a == [0, 1, 2, 3, 4, 5]

def test_already_sorted():
    a = [0, 1, 2, 3, 4, 5]
    my_selection.sort(a)
    assert a == [0, 1, 2, 3, 4, 5]

def test_repeat_elements():
    a = [1, 2, 1, 0, 4, 5, 1, 2]
    my_selection.sort(a)
    assert a == [0, 1, 1, 1, 2, 2, 4, 5]

def test_random():
    n = random.randint(0, 100)
    a = []
    b = []
    for _ in range(n):
        v = random.randint(-100, 100)
        a.append(v)
        b.append(v)
    my_selection.sort(a)
    list.sort(b)
    assert a == b

def test_strings():
    a = ['dog', 'yak', 'cat', 'pig', 'rat', 'owl', 'ant', 'elk' 'cow', 'bee', 'eel', 'gnu', 'ape']
    my_selection.sort(a)
    assert a == ['ant', 'ape', 'bee', 'cat', 'dog', 'eel', 'elkcow', 'gnu', 'owl', 'pig', 'rat', 'yak']
