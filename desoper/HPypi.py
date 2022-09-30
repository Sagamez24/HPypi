#!/usr/bin/env python3
r'''
Hello moduleHPypi module
'''
import dask.array as da
import numpy as np
#from functools import cached_property
#import random
#import sys
#import time
import pandas as pd
from anomalies import anomaly
import itertools
from itertools import permutations
import warnings # ignora los warnings durante compilación
warnings.filterwarnings("ignore")# ignora los warnings durante compilación
global zmax
zmax=30
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
    
def get_solution(l,k,zmax=zmax): #aquí me devuelve q como un diccionario
    q,gcd=_get_chiral( z(l,k) )
    #if q is not None and np.abs(q).max()<=zmax:#
    if q is not None and np.abs(q).max()<=zmax:
        return {'l':l,'k':k,'z':list(q),'gcd':gcd}
    else:
        return {}
    
def get_solution_from_list(lk,zmax=zmax):
    '''
    esta funcion devuelve el vector l+k y el maximo valor que toman
    los elementos de la solucion Z
    '''
    n=len(lk) 
    l=lk[:n//2]
    k=lk[n//2:]
    return get_solution(l,k,zmax)


#assert get_solution_from_list([1,2,1,-2])['z']==[1, 1, 1, -4, -4, 5]

from multiprocessing import Pool
from multiprocessing import cpu_count

def solucion_total(n, M, Nmax, zmax, imax):
    Z_sol = (vector_like(n, M, Nmax))
    print(f'El arreglo vectorlike es:{Z_sol}')
    
    dd=np.arange(0,100)
    size_old=0
    imax=dd[imax]
    i=0
    df=pd.DataFrame()
    Δ_size=1
    #s=time.time()
    
    while Δ_size>-10: 
          Z_sol=Z_sol.compute()
          #print('grid → ',time.time()-s,Z_sol.shape)

          #s=time.time()
          pool = Pool(cpu_count())
          proceso = pool.map(get_solution_from_list, Z_sol)
          pool.close()
          del Z_sol
    
          proceso=[d for d in proceso if d]
          #print('sols → ',time.time()-s,len(proceso))
          df=df.append( proceso )#, ignore_index=True    )  

          df.sort_values('gcd')
          df['zs']=df['z'].astype(str)
          df=df.drop_duplicates('zs').drop('zs',axis='columns').reset_index(drop=True)

          #if n==5:
           #  assert df.shape==(11,4)
          #elif n==6:
          #   assert df.shape==(141,4)
          print('unique solutions → ',df.shape)
          Δ_size=df.shape[0]-size_old
          if Δ_size>0:
             size_old=df.shape[0]
          if i>=imax:
             break
    return df
    
#if __name__ == '__main__':
#    r'''
#    Hello main
#    '''
#    hello()
