


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

    @property
    def group(self):
        return self._group



''' -------------------------- TEST -------------------------- '''
def test_do_making_mandal():
    m = Mandalart('core')
    m.set_position_with_keyword(1, 'computer')
    section = m.get_by_position(1)
    assert section.descr == 'computer', f"{m.group}"

