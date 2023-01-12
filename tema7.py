from abc import abstractmethod

class FormeGeometrice:
    pi = 3.14
    @abstractmethod
    def aria(self):
        pass
    def descrie(self):
        print('cel mai probabil am colturi')

class Patrat(FormeGeometrice):
    def __int__(self,latura=0):
         self._latura=latura
    @property
    def latura(self):
        return self.latura
    def get_latura(self):
        return self._latura
    def set_latura(self,x):
        self._latura=x

    def del_latura(self):
        #del self._latura
        self._latura=None

    def aria(self):
      return self._latura*self._latura


class Cerc(FormeGeometrice):
    def __int__(self, raza):
        self._raza = raza

    def get_raza(self):
        return self._raza

    # @raza.setter
    def set_raza(self, x):
        self._raza = x

    def del_raza(self):
        print('Am sters valoarea')
        #del self._raza
        self._raza=0
    def aria(self):
        return self._raza * self._raza*self.pi
    def descrie(self):
        print('Eu nu am colturi')

f1 = Patrat()
f1.set_latura(10)
print(f1.aria())
f2 = Cerc()
f2.set_raza(5)
print(f2.aria())
f1.descrie()
f2.descrie()
