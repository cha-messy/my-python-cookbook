# -*- coding: utf-8 -*-

def property_example():
    class SetProperty(object):
        # @property
        def Setx(self, value): self._x = value
        def Getx(self, ): return self._x
        def Delx(self, ): del self._x
        x = property(Getx, Setx, Delx, 'attribute x docs')
        
    class SetPropertyByDecorator(object):
        # @property
        def __init__(self, ):
            self._x = None
        @property
        def x(self, ): return self._x
        @x.setter
        def x(self, value): self._x = value
        @x.deleter
        def x(self, ): del self._x
        
    spb = SetPropertyByDecorator()
    print spb.x

if __name__ == '__main__':
    property_example()