#!/usr/bin/env python3
r'''
Hello moduleHPypi module
'''
import dask.array as da
import random
from itertools import permutations

#def hello():
#    r'''
#    Hello function
#    '''
#    return 'Hello, World!'

def valor_m(n):
    """
    valor_m muestra el la cantidad de L y K que se produciran 
    """
    if n%2==0:
        m = n/2 -1
    else:
        m = (n-3)/2
    return m

def vector_like(n, M, Nmax):
    """
    Esta funcion devuelve los vetoreslikes v_mas y v_menos o u_mas y u_menos
    a partir de los arreglos L y K tomados de la lista aleatoria con valores
    entre -15 y 15
    """
    m = int(valor_m(n))
   
#    print(lista)
     
    if n%2 == 0:
        
        lista = da.random.randint(-M, M+1, (Nmax, 2*m)) 
        lista = lista.to_dask_dataframe().drop_duplicates().to_dask_array()
       
        Z_sol=lista
                
    else:
        lista = da.random.randint(-M, M+1, (Nmax, 2*m+1)) 
        lista = lista.to_dask_dataframe().drop_duplicates().to_dask_array()
      

        Z_sol=lista              
    return Z_sol
#if __name__ == '__main__':
#    r'''
#    Hello main
#    '''
#    hello()
