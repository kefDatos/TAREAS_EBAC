#USO DE FUNCIONES LAMBDAS
import math
from functools import reduce

#Función lambda para obtener la raíz cuadrada de un número.
raiz= lambda a: math.sqrt(a)
print(raiz(12))

#Función map, para obtener el largo de una cadena de palabras. 

palabras= 'Estas palabras seran divididas'
lista=palabras.split()
resultado=list(map(len,lista))
print(resultado)

#Función reduce, que sirva para calcular el producto de una lista 
lista=[1,2,3,4]
Producto = reduce(lambda x, y: x * y, lista)
print(Producto)

#Función filter que sirva para encontrar palabras que contengan mayúsculas o números en un listado
def mayus(x):
    return x[0].isupper()
           

listado=['Yo','ejemplo',3,4.5,'Canada','ejercicio',0]

filtrado = list(filter(lambda x:isinstance(x, (int, float)) or mayus(x), listado))
print(filtrado)