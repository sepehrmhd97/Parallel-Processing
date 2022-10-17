#!/usr/bin/env python3.9

from person import Person
from time import perf_counter as pc
import matplotlib.pyplot as plt
from numba import njit

def fib_py(n):
    if n <= 1:
        return n
    else:
        return (fib_py(n-2) + fib_py(n-1)) 
    
@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return (fib_numba(n-2) + fib_numba(n-1))


def main():
    xlist = [i for i in range(20,31)]
    ylist_py = []
    ylist_numba = []
    ylist_c = []
    
    for i in xlist:
        start = pc()
        fib_py(i)
        end = pc()
        ylist_py.append(end -start)
        
        start = pc()
        fib_numba(i)
        end = pc()
        ylist_numba.append(end -start)
        
        start = pc()
        Person.fib_c(i)
        end = pc()
        ylist_c.append(end -start)
        
    print(ylist_py)
    print(ylist_numba)
    print(ylist_c)
        
        

if __name__ == '__main__':
	main()
