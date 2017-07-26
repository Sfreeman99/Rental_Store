from core import *

def test_remove_one_atv():
    assert (remove_stock(1, 'Atv', {'Atv':{'price': 30, 'stock': 5}}) ==
            {'Atv': {'price': 30, 'stock': 4}})

def test_remove_atv_with_more_than_one_dict():
    assert (remove_stock(1, 'Atv', {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price': 100, 'stock': 5}}) ==
            {'Atv':{'price': 30, 'stock': 4}, 'Side-by-Side':{'price':100, 'stock': 5}})

def test_remove_one_sbs():
    assert (remove_stock(1, 'Side-by-Side', {'Side-by-Side':{'price': 30, 'stock': 5}}) ==
            {'Side-by-Side': {'price': 30, 'stock': 4}})

def test_remove_sbs_with_more_than_one_dict():
    assert (remove_stock(1, 'Side-by-Side', {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price': 100, 'stock': 5}}) ==
            {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price':100, 'stock': 4}})
    