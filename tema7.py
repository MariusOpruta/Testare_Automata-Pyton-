from abc import ABC

def abstractmetrod(abc):
    pass


class FormeGeometrice(ABC):
    PI = 3.14

    @abstractmetrod
    def aria(self):
        raise


    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormeGeometrice):
    def __int__(self, latura):
        self.latura=latura

    @property
    def latura(self):
        return self.latura

    @latura.getter
    def get_latura(self):
        print(f'Latura este {self.latura}')
        return self.latura

    @latura.setter
    def set_latura(self, latura):
        print(f'Latura devine {self.latura}')
        self.latura = latura

    @latura.deleter
    def del_latura(self):
        print(f'Am sters valoarea:')
        del self.latura
    def get_aria(self):
        return self.get_latura()*self.get_latura()

class Cerc(FormeGeometrice):
    def __int__(self, raza=12):
        self.raza = raza

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
         return self.raza


    @raza.setter
    def raza(self, raza):
         self.raza = raza



    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea')
        del self.raza
    def ariacerc(self):
        return self.raza * self.raza * self.PI
f1 = Cerc()
print(f1)

