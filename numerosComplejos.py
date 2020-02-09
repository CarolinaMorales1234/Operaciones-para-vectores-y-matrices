"""
*Autor: Carolina Morales
*Libreria numeros complejos
*Asignatura: CNYT-1
*Descripción: Demo de una libreria para realizar operaciones con numeros complejos como la suma, resta, multiplicacion, division, el modulo,
el conjugado, la conversion de polar a cartesiano y viceversa y la potencia de un numero complejo.
"""

from sys import stdin
import math

#PARTE 1

def sumar(a,b):
    """
    Descripción: Función encargada de sumar dos numeros complejos
    Input: dos arreglos de la forma [a,b]
    Output: devuelve el resultado de la opercion de la forma a+bi
    """
    suma=a[0]+b[0]
    suma2=a[1]+b[1]
    return suma,suma2

    
##    if suma2>=0:
##        return str(suma)+'+'+str(suma2)+'i'
##    else:
##        return str(suma)+str(suma2)+'i'
def restar(a,b):
    """
    Descripción: Función encargada de restar dos numeros complejos
    Input: dos arreglos de la forma [a,b]
    Output: devuelve el resultado de la opercion de la forma a+bi
    """
    resta=a[0]-b[0]
    resta1=a[1]-b[1]
    return resta,resta1
def multiplicar(a,b):
    """
    Descripción: Función encargada de multiplicar dos numeros complejos
    Input: dos arreglos de la forma [a,b]
    Output: devuelve el resultado de la opercion de la forma a+bi
    """
    mult1=a[0]*b[0]+(-1*(a[1]*b[1]))
    mult2=a[0]*b[1]+a[1]*b[0]
    if mult2<0:
        mult1,mult2
    else:
        return mult1,mult2

def dividir(a,b):
    """
    Descripción: Función encargada de dividir dos numeros complejos
    Input: dos arreglos de la forma [a,b]
    Output: devuelve el resultado de la opercion de la forma (a+bi)/c
    """
    new=(b[1]*-1)
    b_nuevo=[]
    b_nuevo.append(b[0])
    b_nuevo.append(new)
    m1=multiplicar(a,b_nuevo)
    m2=multiplicar(b,b_nuevo)
    return m1,m2[0]+m2[1]
    
def modulo(a):
    """
    Descripción: Función encargada de encontrar el modulo de un numero complejo de la forma a+bi
    Input: un arreglo de la forma [a,b]
    Output: un valor numerico
    """
    raiz=math.sqrt((a[0]**2)+(a[1]**2))
    return raiz

def conjugado(a):
    """
    Descripción: Función encargada de encontrar el conjugado de un numero complejo de la forma a+bi
    Input: un arreglo de la forma [a,b]
    Output: un arreglo con el conjugado de la forma a+bi
    """
    a[1]*=-1
    return [a[0],a[1]]

def polarC(a):
    """
    Descripción: Función encargada de convertir un valor en su forma polar a la forma cartesiana
    Input: un arreglos de la forma [a,b] donde a es la longitud del vector y b el angulo formado
    Output: una tupla que contiene el valor cartesiano de la forma a+bi
    """    
    x=math.radians(a[1])
    y=math.radians(a[1])
    x1=a[0]*math.cos(x)
    y1=a[0]*math.sin(y)
    return x1,y1

def cartesianoP(a):
    """
    Descripción: Funcion encargada de convertir un valor en su forma cartesiana a la forma polar
    Input: Un arreglo de la forma [a,b]
    Output: una tupla de la forma Re^θ
    cartesianoP([-1,1.732])
    """
    r=modulo(a)
    a=math.atan2(a[1],a[0])    
    g=math.degrees(a)
    return r,g

def potencia(a):
    real=(a[0]**2)+((a[1]**2)*-1)
    imag=2*a[0]*a[1]
    return real,imag
    #return str(real)+'+'+str(imag)+'i'
