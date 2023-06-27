class Foo:
    def __init__(self,x=None):
        # self._x é por convenção privada
        self._x = x

    @property
    def x(self):
        # retorna _x ou se nao existir 0
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        self._x += valor 
    
    @x.deleter
    def x(self):
        self._x = 0
    
foo = Foo(10)
# Como é uma propriedade não precisa instanciar foo.x(), pois não é um metodo
print(foo.x)

# Propriedades é usada como uma variavel no programa principal, so temos que definir o comportamento na classe
foo.x = 10
print(foo.x)

# Podemos definir o comportamento de delete da variavel foo.x
del foo.x
print(foo.x)