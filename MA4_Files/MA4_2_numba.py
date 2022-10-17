from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

@njit
def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-2) + fib(n-1))
    
if __name__ == "__main__":
    
    xlist = [i for i in range(15,40)]
    ylist = []
  
    for i in xlist:
        start = pc()
        fib(i)
        end = pc()
        print (fib(i))
        ylist.append(end - start)
        
    plt.plot(xlist, ylist)
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.show() 
    plt.savefig('numba.jpeg') 
    
   