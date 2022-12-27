from abc import ABC


def abstractmetrod(abc):
    pass


class FormeGeometrice(ABC):
    PI = 3.14

    @abstractmetrod
    def aria(self):
        raise

    @abstractmetrod
    def descrie(self):
        raise


class Descrie:
    print('Cel mai probabil am colturi')


class Patrat(FormeGeometrice):
    def __int__(self, latura):
        self.latura = latura

    @property
    def latura(self):
        return self.latura

    @latura.getter
    def latura(self):
        print(f'Latura este {self.latura}')
        return self.latura

    @latura.setter
    def latura(self, latura):
        print(f'Latura devine {self.latura}')
        self.latura = latura

    @latura.deleter
    def latura(self):
        print(f'Am sters valoarea:')
        self.latura = 0


class Cerc(FormeGeometrice):
    def __int__(self, raza):
        self.raza = raza

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
        print(f'Raza este: {self.raza}')
        return self.raza

    @raza.setter
    def raza(self, raza):
        print(f'Raza devine: {self.raza}')
        self.raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea')
        self.raza = 0
