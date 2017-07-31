from core import *

def test_remove_one_atv():
    assert (remove_stock('Atv', {'Atv':{'price': 30, 'stock': 5}}) ==
            {'Atv': {'price': 30, 'stock': 4}})

def test_remove_atv_with_more_than_one_dict():
    assert (remove_stock('Atv', {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price': 100, 'stock': 5}}) ==
            {'Atv':{'price': 30, 'stock': 4}, 'Side-by-Side':{'price':100, 'stock': 5}})

def test_remove_one_sbs():
    assert (remove_stock('Side-by-Side', {'Side-by-Side':{'price': 30, 'stock': 5}}) ==
            {'Side-by-Side': {'price': 30, 'stock': 4}})

def test_remove_sbs_with_more_than_one_dict():
    assert (remove_stock('Side-by-Side', {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price': 100, 'stock': 5}}) ==
            {'Atv':{'price': 30, 'stock': 5}, 'Side-by-Side':{'price':100, 'stock': 4}})

def test_sales_tax():
    assert sales_tax(3) == 3.21
    assert sales_tax(2) == 2.14
    assert sales_tax(1) == 1.07
    assert sales_tax(0) == 0

def test_total_for_one_atv():
    assert total(1, 'Atv',{'Atv':{'rental price': 30, 'stock': 5}}) == 30

def test_total_for_two_atvs():
    assert total(2,'Atv', {'Atv':{'rental price': 30, 'stock': 5}}) == 60

