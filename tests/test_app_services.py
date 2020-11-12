import pytest

from app.services import *

@pytest.fixture 
def instance():
    return Mandalart("core")

def test_do_making_mandal(instance):
    '''
    test - making mandalart by new section  
    '''
    m = instance
    m.set_position_with_keyword(1, "computer")
    section = m.get_by_position(1)
    assert section.descr == "computer", f"{m.group}"

'''

1. testing for the register of mandalart by 1 keyword
2. testing for the register of mandalart by 2 keyword
3. testing for the register of mandalart by 4 keyword
4. testing for the register of mandalart by 8 keyword

'''

def test_register_of_mandalart_by_1_keyword(instance):
    instance.set_position_with_keyword(1, "car")
    section = instance.get_by_position(1)
    assert section.descr == 'car'

def test_register_of_mandalart_by_2_keyword(instance):
    instance.set_position_with_keyword(1, "car_1")
    instance.set_position_with_keyword(2, "car_2")
    section = instance.get_by_position(1)
    assert section.descr == 'car_1'
    section = instance.get_by_position(2)
    assert section.descr == 'car_2'

def test_register_of_mandalart_by_4_keyword(instance):
    instance.set_position_with_keyword(1, "car_1")
    instance.set_position_with_keyword(2, "car_2")
    instance.set_position_with_keyword(3, "car_3")
    instance.set_position_with_keyword(4, "car_4")
    section = instance.get_by_position(1)
    assert section.descr == 'car_1'
    section = instance.get_by_position(2)
    assert section.descr == 'car_2'
    section = instance.get_by_position(3)
    assert section.descr == 'car_3'
    section = instance.get_by_position(4)
    assert section.descr == 'car_4'

def test_register_of_mandalart_by_8_keyword(instance):
    instance.set_position_with_keyword(1, "car_1")
    instance.set_position_with_keyword(2, "car_2")
    instance.set_position_with_keyword(3, "car_3")
    instance.set_position_with_keyword(4, "car_4")
    instance.set_position_with_keyword(5, "car_5")
    instance.set_position_with_keyword(6, "car_6")
    instance.set_position_with_keyword(7, "car_7")
    instance.set_position_with_keyword(8, "car_8")
    section = instance.get_by_position(1)
    assert section.descr == 'car_1'
    section = instance.get_by_position(2)
    assert section.descr == 'car_2'
    section = instance.get_by_position(3)
    assert section.descr == 'car_3'
    section = instance.get_by_position(4)
    assert section.descr == 'car_4'
    section = instance.get_by_position(5)
    assert section.descr == 'car_5'
    section = instance.get_by_position(6)
    assert section.descr == 'car_6'
    section = instance.get_by_position(7)
    assert section.descr == 'car_7'
    section = instance.get_by_position(8)
    assert section.descr == 'car_8'


