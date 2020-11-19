import json 

import abc 

class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod 
    def operation(self):
        pass


class Composite(Component):
    '''
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the component interface 
    '''
    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)

class Leaf(Component):
    '''
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    '''
    def operation(self):
        pass 


class Mandal(metaclass=abc.ABCMeta):
    @abc.abstractmethod 
    def operation(self):
        pass


class MandalMaster(Mandal):
    def __init__(self):
        self._mandalart = set()
    def add(self, mandal):
        pass



class MandalartSection:
    def __init__(self, position : int, descr : str):
        self._position = position 
        self._descr = descr 

    @staticmethod
    def make_default(position : int):
        return MandalartSection(position, '')

    @staticmethod
    def make_default_with_descr(position : int, descr : str):
        return MandalartSection(position, descr)

    @property
    def position(self):
        return self._position

    @property
    def descr(self):
        return self._descr 
    
    def __iter__(self):
        yield 'position', self.position
        yield 'descr', self.descr
    
    def __str__(self):
        return f"position : {self.position}, descr : {self.descr}"

class Mandalart(MandalartSection):
    def __init__(self, descr : str ):
        super().__init__(0, descr)
        self._group = { 
            0 : self
            , 1 : MandalartSection.make_default(1)
            , 2 : MandalartSection.make_default(2)
            , 3 : MandalartSection.make_default(3)
            , 4 : MandalartSection.make_default(4)
            , 5 : MandalartSection.make_default(5)
            , 6 : MandalartSection.make_default(6)
            , 7 : MandalartSection.make_default(7)
            , 8 : MandalartSection.make_default(8)
        }
        self._descr = descr 
    
    def __validation_check_position(self, position):
        if position < 1 and postion > 8:
            raise ValueError("Values can only accept values between 1 and 8")

    def set_position_with_keyword(self, position : int, descr : str):
        self.__validation_check_position(position)
        self._group[position] = MandalartSection.make_default_with_descr(position, descr)

    def get_by_position(self, position : int):
        self.__validation_check_position(position)
        section = self._group[position]
        return section

    def debug(self):
        display_ = f'''
        [-] position 0 = {self._group[0].descr}
            - position 1 = {self._group[1].descr}
            - position 2 = {self._group[2].descr}
            - position 3 = {self._group[3].descr}
            - position 4 = {self._group[4].descr}
            - position 5 = {self._group[5].descr}
            - position 6 = {self._group[6].descr}
            - position 7 = {self._group[7].descr}
            - position 8 = {self._group[8].descr}
        '''
        return display_
 
    def __iter__(self):
        yield 0 , self.group[0].descr
        yield 1 , self.group[1].descr
        yield 2 , self.group[2].descr
        yield 3 , self.group[3].descr
        yield 4 , self.group[4].descr
        yield 5 , self.group[5].descr
        yield 6 , self.group[6].descr
        yield 7 , self.group[7].descr
        yield 8 , self.group[8].descr
    
    @staticmethod 
    def create_mandal(core : str, keywords : list ):
        m = Mandalart(core)
        for idx, val in enumerate(keywords[:8]):
            m.set_position_with_keyword((idx+1), val)
        return m 
    
    @property
    def group(self):
        return self._group


if __name__ == '__main__':
    m = Mandalart('core')
    m.set_position_with_keyword(1, 'like')
    print(dict(m))
    
    m = Mandalart.create_mandal('car', "BCDEFGHIKKKK")
    print(dict(m))


