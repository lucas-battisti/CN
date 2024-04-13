import numpy as np
from IPython.display import display, Latex
from typing import Union, Optional

def base_N_to_decimal_int(input: int, N: int=2, verbose: bool=False):
    
    input_str = np.array([int(x) for x in str(input)])
    
    powers = np.array([N**k for k in range(len(input_str)-1, -1, -1)])
    
    result = np.dot(input_str, powers)
    
    if verbose:
        
        powers_str = str(['{}^{}'.format(N, k) for k in range(len(input_str)-1, -1, -1)])
        
        print(str(list(input_str)) + " * " + powers_str + "=")
        print(str(list(input_str)) + " * " + str(list(powers)))
        print("= {}".format(result))
    else:
        print(str(result))

        
def decimal_to_base_N_int(input: int, N: int=2, verbose: bool=False):
    
    dividends = [input]
    
    quocients = [None]
    remainders = []
    
    while quocients[-1] != 0 and len(quocients) < 10:
        
        quocients.append(dividends[-1] // N)
        remainders.append(dividends[-1] % N)
        
        if quocients[-1] != 0:
            dividends.append(quocients[-1])
            
    quocients.pop(0)
            
    if verbose:
        
        for i in range(len(dividends)):
            print("{} ÷ {} = {} (resto = {})".format(dividends[i], N, quocients[i], remainders[i]))
    
    remainders.reverse()
    print(str(remainders))
    
def decimal_to_base_N_float(input: float, N: int=2, t: int = 10, verbose: bool=False):

    input = np.abs(input)
    
    mantissas = [input]
    ineq = []
    
    if np.emath.logn(1/N, input) % 1 == 0:
        print("0.1 * {}^{}".format(N, np.emath.logn(1/N, input)+1))
        #return
    
    if input > 1:
        
        ineq = ['>']
        e = 1
        
        while mantissas[-1] > 1:
            ineq.append('>')
            mantissas.append(mantissas[0]/(N**e))
            e += 1
            
        ineq[-1] = '<'
        mantissa = mantissas[-1]
        
    if input < 1:
        
        ineq = ['<']
        e = -1
        
        while mantissas[-1] < 1:
            ineq.append('<')
            mantissas.append(mantissas[0]/(N**e))
            e -= 1
            
        ineq[-1] = '>'
        mantissa = mantissas[-2]
        e += 2
        
        
    d = []
    mantissas2 = [mantissa]
    
    while len(d) < t:
        
        d.append(N*mantissas2[-1] // 1)
        
        mantissas2.append(N*mantissas2[-1] - d[-1])
    
    if verbose:   
        for i in range(len(mantissas)):
        
            if e < 0:
                ii = -i
        
            print("{}/({}^{}) = ".format(input, N, ii)
                + str(mantissas[i]) + ineq[i] + "1")
        
        print("\n")
        print("e = {}".format(e))
        print("mantissa é {}".format(mantissa))
        print("\n")
    
        for i in range(len(d)):
            print(str(mantissas2[i]) +
                  " = d = d{} {}^-1 + d{} {}^-2 + ...".format(i+1, N, i+2, N))
            print("\n")
            print(str(N*mantissas2[i]) +
                  " = {}d = d{} + d{} {}^-2 + ...".format(N, i+1, N, i+2, N))
            print("\n")
            print("Deduzimos que d{} é igual à parte inteira de {}d:".format(i+1, N))
            print(" d{} = int({}) = {}".format(i+1, N*d[i], d[i]))
            print("\n")
            print("Agora redefinimos d subtraindo-o à d{}".format(i+1))
            print("d <- d - d{} = {}".format(i+1, mantissas2[i+1]))
            print("\n")

    print(str(d) + "* {}^{}".format(N, e))

def decimal_to_base_N(input: Union[int, float], N: int=2, t: Optional[int] = 10, verbose: bool=False):
    if isinstance(input, int):
        decimal_to_base_N_int(input=input,N=N,verbose=verbose)
    if isinstance(input, float):
        decimal_to_base_N_float(input=input,N=N,t=t,verbose=verbose)
    
def SNPF_info(b:int, t:int, m:int, M:int):
    
    c = 2*(M + m + 1)*(b - 1) * b**(t-1) + 1
    eps = b**(1-t)
    min = b**(-1-m)
    max = b**(t-1) * b**(M-t)
    
    print('Cardinalidade: 2*(M + m + 1)(β - 1) * β^(t-1) + 1 =')
    print(c)
    print('Epsilon: β^(1-t) =')
    print(eps)
    print('Menor: β^(-1-m) =')
    print(min)
    print('Maior: (β^t-1)β^(M-t) =')
    print(max)
    
    

