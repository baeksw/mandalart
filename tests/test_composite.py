import pytest 

from app.services import *

def test_composition():
    leaf = Leaf()
    composite = Composite()
    composite.add(leaf)
    composite.operation()

    assert False
