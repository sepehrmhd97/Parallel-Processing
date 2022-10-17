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
    l = Person(n)
    
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
        l.fib_c(l.get())
        end = pc()
        ylist_c.append(end -start)
        
    # print(ylist_py)
    # print(ylist_numba)
    # print(ylist_c)
    plt.plot(xlist,ylist_py,label = "python")
    plt.plot(xlist,ylist_py,label = "numba")
    plt.plot(xlist,ylist_c,label = "c++")
    plt.yscale('log')
    plt.legend()
    plt.savefig('figure.png')
        
        

if __name__ == '__main__':
	main()
