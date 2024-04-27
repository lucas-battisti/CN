import numpy as np
from IPython.display import display, Latex
from typing import Union, Optional


def bisses(f: function, a: float, b: float,
           max_iter: int, err: Union[float, int],
           verbose: bool = False):
    
    if err.isinstance(int):
        err = 0.5*10**(-err)
        
    print("a0 = {},     b0 = {}".format(a, b))
        
    
    for k in range(max_iter):
        c = np.mean(a, b)
        
        fa = f(a)
        fb = f(b)
        
        if fa*fb > 0:
            raise ValueError("f(a{})*f(b{}) > 0".format(k, k))
        
        fc = f(c)
        
        if fa*fc < 0 and fb*fc > 0:
            new_a = "a", a
            new_b = "c", c
            one = 0
        
        if fb*fc < 0 and fa*fc > 0:
            new_a = "c", c
            new_b = "b", b
            one = 1
            
        
        if verbose:
            
            print("c{} = {}".format(k, c))
            
            print("f(a{}) = {},     f(b{}) = {},     f(c{}) = {}".format(k, fa, k, fb, k, fc))
            
            print("f({})*f(c) < 0 e f({})*f(c) > 0 -->".format(["a", "b"][one], ["a", "b"][1 - one])
                  +" {}{} = {}{} ".format("a", k+1, new_a[0], k) +
                  "e {}{} = {}{}".format("b", k+1, new_b[0], k))
            
            
        a, b = new_a[1], new_b[1]
        
        
    
    