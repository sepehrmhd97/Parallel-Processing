import numpy as np
import math


def d_dimen_vol (n, d):
    exact_vol = []
    app_vol = []
    r = []
    x = lambda a: np.sqrt(np.sum(a**2))
    for i in range(n):
        rad_rand = np.random.uniform(-1,1, d)
        r.append(x(rad_rand))
    exact_vol.append((math.pi ** (d/2)) / math.gamma(d/2 + 1))
    cube_vol = 2 ** d
    circle = list(filter(lambda a: a <= 1 , r))
    app_vol.append((len(circle) / n) * cube_vol)
    for e, a in zip(exact_vol, app_vol):
        print ('for d = {} and n = {}: Exact Volume = {}, Approximate Volume = {}'.format(d,n,e,a))
        
        
#def main():
    
    
        
if __name__ == "__main__":
    d_dimen_vol(100000,11)