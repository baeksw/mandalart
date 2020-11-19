import pytest 
import numpy as np
import pandas as pd 


def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5


@pytest.mark.parametrize('dtype',['int8','int6','int32','int64'])
def test_dtypes(dtype):
    assert str(np.dtype(dtype)) == dtype 


