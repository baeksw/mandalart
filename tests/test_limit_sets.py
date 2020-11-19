import json
import abc

from collections import deque



class Mandal:

    def __init__(self, pos : int, descr : str):
        self._pos = pos
        self._descr = descr 
    
    @property
    def position(self):
        return self._pos 

    @property
    def descr(self):
        return self._descr 

    @position.setter
    def position(self, pos):
        self._pos = pos 

    @descr.setter
    def descr(self, descr):
        self._descr = descr
    
    @staticmethod
    def make_default(pos : int, descr : str):
        return Mandal(pos, descr)
    
    def __hash__(self):
        return self.position

    def __eq__(self, obj):
        valid = [
            self._pos == obj.position
            , self._descr == obj.descr
        ]
        return all(valid)

    def __str__(self):
        return f"{self._pos} : [{self._descr}] "

    def __iter__(self):
        yield "position" , self._pos
        yield "desc", self._descr

    @abc.abstractmethod
    def operation(self):
        pass 


class MandalSection(Mandal):
    def __init__(self,pos : int = 0,  descr : str = ''):
        super().__init__(pos , descr)

    def operation(self):
        print(f"\t - {self._pos} : [{self._descr}] ")

class MandalCore(Mandal):
    def __init__(self, descr : str = ''):
        super().__init__(0 , descr)
        self._set = set()
        self._set.add(Mandal(0, descr))

    def add(self, mandal : Mandal):
        assert mandal.position > 0 and mandal.position < 9, f"pos = {mandal.position}"
        self._set.add(mandal)

    def remove(self, mandal : Mandal):
        self._set.discard(mandal)

    def operation(self):
        print(f"({len(self._set)}){self.position} - {self.descr}")

        for mandal in self._set:
            mandal.operation()
    
# -- main --

if __name__ == 'x__main__':
    '''
    '''
    m = MandalCore()
    m.descr = 'core'
    m.add(MandalSection(1,'0110'))
    m.add(MandalSection(2,'0220'))
    m.add(MandalSection(3,'0330'))
    m.add(MandalSection(4,'0440'))
    m.add(MandalSection(5,'0550'))
    m.add(MandalSection(6,'0660'))
    m.add(MandalSection(7,'0770'))
    m.add(MandalSection(8,'0880'))

    m2 = MandalCore('house')
    m2.add(MandalSection(1,'1a'))
    m2.add(MandalSection(2,'2a'))
    m2.add(MandalSection(3,'3a'))
    m2.add(MandalSection(4,'4a'))
    m2.add(MandalSection(5,'5a'))
    m2.add(MandalSection(6,'6a'))
    m2.add(MandalSection(7,'7a'))
    m2.operation()



class MandalDomain:

    def __init__(self):
        self._elements = set()
    
    @property
    def elements(self):
        return self._elements

    def add(self, position, mandal : Mandal):
        mandal.position = position 
        self._elements.add(mandal)
        return self

class DisplayMandal:

    def __init__(self, model : MandalDomain):
        self._model = model

    def display(self):
        for mandal in self._model.elements:
            print(mandal)


if __name__ == '__main__':
    domain = MandalDomain()
    domain \
        .add(1, Mandal(1, 'A1')) \
        .add(2, Mandal(2, 'A2')) \
        .add(3, Mandal(3, 'A3')) \
        .add(4, Mandal(4, 'A4')) \
        .add(5, Mandal(5, 'A5')) \
        .add(6, Mandal(6, 'A6')) \
        .add(7, Mandal(7, 'A7')) \
        .add(8, Mandal(8, 'A8')) 

    DisplayMandal(domain).display()


# -- tests --

def test_compare_instance_of_mandal_sections():
    m1 = MandalSection(1, '111')
    m2 = MandalSection.make_default(1, '111')
    assert m1 == m2

def test_make_and_add_set():
    m1 = MandalSection(1, '111')
    m2 = MandalSection.make_default(1, '111')
    m3 = MandalSection.make_default(2, '111')
    sets = set()
    sets.update([m1,m2, m3])
    sets.add(m1)
    sets.add(m2)
    sets.add(m3)
    assert len(sets) == 2

