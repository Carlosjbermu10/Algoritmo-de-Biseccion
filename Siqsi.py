# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 04:29:51 2022

@author: CarLosMiX

Carlos bermudez 29668441
"""

print ("ALGORTMO DE BISECCION") 

import math

funcion = input("Ingrese la Funcion: ")
a = float(input("Ingrese el rango de la Funcion(Valor mas bajo): "))
b = float(input("Ingrese el rango de la Funcion(Valor mas alto): "))
tolerancia = float(input("Ingrese el error Relativo: "))

def resolver_funcion(x):
    return eval(funcion)

er = 9999999999
valor_anterior = 0
i = 0

if (resolver_funcion(a) * resolver_funcion(b)) < 0:
    
    while er >= tolerancia:
    
        puntoMedio = (a+b)/2
        funcion_a = resolver_funcion(a)
        funcion_b = resolver_funcion(b)
        funcion_c = resolver_funcion(puntoMedio)
        
        i += 1      
    
        print()
        print("Esta es la Iteracion, Nro: ", i)
        print("Valor a: ", a, " Valor b: ", b, " Punto medio: ", puntoMedio, " Error Relativo: ", er)
    
        if funcion_c < 0:
            a = puntoMedio
        else:
            b = puntoMedio
    
        er =  abs((puntoMedio - valor_anterior)/puntoMedio)
        valor_anterior = puntoMedio
else:
    print ("Error para el calculo")
    print ("No se culple el Teorema del Valor Intermedio o el Teorema de Contunuidad")
    


print()
print()
print("La Funcion", funcion, " se vuelve Cero, Aproximadamente en: ", puntoMedio)
    
