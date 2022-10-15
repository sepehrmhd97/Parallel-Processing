from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-2) + fib(n-1))
    
if __name__ == "__main__":
    #n = range(30,41)
    xlist = [i for i in range(5,10)]
    ylist = []
    #print(xlist)
    for i in xlist:
        start = pc()
        fib(i)
        end = pc()
        ylist.append(end - start)
        
    plt.plot(xlist, ylist)
    plt.xlabel('N')
    plt.ylabel('Time')
    #plt.show() 
    plt.savefig('purepython.jpeg') 
    
    #print(ylist)