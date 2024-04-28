import numpy as np
from typing import Union, Callable


def bisses(f: Callable[[float], float],
           a: float, b: float,
           max_iter: int, err: Union[float, int],
           verbose: bool = False):
    
    if isinstance(err, int):
        err = 0.5*10**(-err)
        
    c = []
    
    for k in range(max_iter):
        c.append((a+b)/2)
        
        fa = f(a)
        fb = f(b)
        
        if fa*fb > 0:
            raise ValueError("f(a{})*f(b{}) > 0".format(k, k))
        
        fc = f(c[k])
        
        if fa*fc < 0 and fb*fc > 0:
            new_a = "a", a
            new_b = "c", c[k]
            one = 0
        
        if fb*fc < 0 and fa*fc > 0:
            new_a = "c", c[k]
            new_b = "b", b
            one = 1
        
        if fc == 0:
            print("f(c{}) = 0.0".format(k))
            return c
            
        
        if verbose:
            print("a{} = {},     b{} = {}".format(k, a, k, b))
            
            print("c{} = {}".format(k, c[k]))
            
            print("f(a{}) = {},     f(b{}) = {},     f(c{}) = {}".format(k, fa, k, fb, k, fc))
            
            print("f({})*f(c) < 0 e f({})*f(c) > 0 -->".format(["a", "b"][one], ["a", "b"][1 - one])
                  +" {}{} = {}{} ".format("a", k+1, new_a[0], k) +
                  "e {}{} = {}{}".format("b", k+1, new_b[0], k))
            
            print("---------------------------------------------------")
                
                
        if len(c) > 1 and abs(c[k] - c[k-1]) < err:
            print("|c{} - c{}| < {}".format(k, k-1, err))
            return c[k]
            
        a, b = new_a[1], new_b[1]
        
    
    print("Chegou a máximo de iterações (max_iter)")
    return c[-1]

def mils(phi: Callable[[float], float],
         x0: float,
         max_iter: int, err: Union[float, int],
         verbose: bool = False):
    
    if isinstance(err, int):
        err = 0.5*10**(-err)
        
    x = [x0]
    
    for k in range(max_iter):
        
        phixk = phi(x[k])
        
        if phixk == 0:
            print("φ(x{}) = 0.0".format(k))
            return x[k]
            
        
        x.append(phixk)
        
        if verbose:
            print("x{} = {}".format(k, x[k]))
            
            print("x{} = φ(x{}) = {}".format(k+1, k, phixk))
            
            print("---------------------------------------------------")
        
        if len(x) > 1 and abs(x[k] - x[k+1]) < err:
            print("|x{} - x{}| < {}".format(k, k+1, err))
            return x[k+1]
        
    print("Chegou a máximo de iterações (max_iter)")
    return x[-1]
    
    


def newton(f: Callable[[float], float], df: Callable[[float], float],
           x0: float,
           max_iter: int, err: Union[float, int],
           verbose: bool = False):
    
    if isinstance(err, int):
        err = 0.5*10**(-err)
        
    x = [x0]
    
    for k in range(max_iter):
        
        fxk = f(x[k])
        dfxk = df(x[k])
        
        if fxk == 0:
            print("f(x{}) = 0.0".format(k))
            return x[k]
            
        
        x.append(x[k] - fxk/dfxk)
        
        if verbose:
            print("x{} = {}".format(k, x[k]))
            
            print("x{} = x{} - f(x{})/f'(x{}) =".format(k+1, k, k, k))
            print("{} - {}/{} = {}".format(x[k], fxk, dfxk, x[k+1]))
            
            print("---------------------------------------------------")
        
        if len(x) > 1 and abs(x[k] - x[k+1]) < err:
            print("|x{} - x{}| < {}".format(k, k+1, err))
            return x[k+1]
        
    print("Chegou a máximo de iterações (max_iter)")
    return x[-1]
    
def secante(f: Callable[[float], float],
           x0: float, x1: float,
           max_iter: int, err: Union[float, int],
           verbose: bool = False):
    
    if isinstance(err, int):
        err = 0.5*10**(-err)
        
    x = [x0, x1]
    
    for k in range(max_iter):
        
        f0 = f(x[k])
        f1 = f(x[k+1])
        
        if fxk == 0:
            print("f(x{}) = 0.0".format(k))
            return x[k]
            
        
        x.append((x[k]*f1 - x[k+1]*f0)/(f1-f0))
        
        if verbose:
            print("x{} = {}".format(k, x[k]))
            print("x{} = {}".format(k+1, x[k+1]))
            
            print("x{} = (x{}*f(x{}) - x{}*f(x{}))/(f(x{})-f(x{})) =".format(k+2, k, k+1, k+1, k, k+1, k))
            print("{}/{} = {}".format((x[k]*f1 - x[k+1]*f0), (f1-f0),  x[k+2]))
            
            print("---------------------------------------------------")
        
        if len(x) > 1 and abs(x[k+1] - x[k+2]) < err:
            print("|x{} - x{}| < {}".format(k+1, k+2, err))
            return x[k+2]
        
    print("Chegou a máximo de iterações (max_iter)")
    return x[-1]
    