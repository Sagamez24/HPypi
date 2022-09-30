#!/usr/bin/env python3
r'''
Hello moduleHPypi module
'''
import dask.array as da
import numpy as np
#from functools import cached_property
#import random
from anomalies import anomaly
import itertools
from itertools import permutations
import warnings # ignora los warnings durante compilación
warnings.filterwarnings("ignore")# ignora los warnings durante compilación

#def hello():
#    r'''
#    Hello function
#    '''
#    return 'Hello, World!'

z=anomaly.free

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

def _get_chiral(q,q_max=np.inf):
    #Normalize to positive minimum
    if 0 in q:
        return None,None  #Quita los ceros
    if q[0]<0:
        q=-q
    #Divide by GCD
    GCD=np.gcd.reduce(q)
    q=(q/GCD).astype(int)
    if ( 0 not in [ sum(p) for p in itertools.permutations(q, 2) ] and np.abs(q).max()<=q_max):
        return q,GCD #not 0 in q, #avoid vector-like and multiple 0's ##De todos los elementos 
                      #de q, tome el más grande y positivo y menor que infinito
    else:
        return None,None
    
def get_solution(l,k,zmax=30): #aquí me devuelve q como un diccionario
    q,gcd=_get_chiral( z(l,k) )
    #if q is not None and np.abs(q).max()<=zmax:#
    if q is not None and np.abs(q).max()<=zmax:
        return {'l':l,'k':k,'z':list(q),'gcd':gcd}
    else:
        return {}
    
def get_solution_from_list(lk,zmax=32):
    n=len(lk)
    l=lk[:n//2]
    k=lk[n//2:]
    return get_solution(l,k,zmax)


assert get_solution_from_list([1,2,1,-2])['z']==[1, 1, 1, -4, -4, 5]
    
#if __name__ == '__main__':
#    r'''
#    Hello main
#    '''
#    hello()
