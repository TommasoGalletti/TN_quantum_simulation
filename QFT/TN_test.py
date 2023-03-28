import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import quimb as qu
import quimb.tensor as qtn

def build_QFT(N, regs):
    for i in range(N):
        circ.apply_gate('H', regs[i])                               
        for j in range(i + 1, N):
            theta = np.pi / 2 ** (j - i)    #rotation angle   
            circ.apply_gate('CU1', theta, regs[i], regs[j])
                
    for i in range(N // 2):
        circ.apply_gate('SWAP', regs[i], regs[N - i - 1])


maxqubit = 6       #37
nsampling = 10   #100k ?
 
N = maxqubit

regs = list(range(N))
circ = qtn.Circuit(N)

build_QFT(N, regs)

bigmatrix = np.zeros((nsampling, N), np.int8)

row = 0
for b in circ.sample(nsampling):
    
    shot = list(b)
    bigmatrix[row] = shot
    row += 1

print(bigmatrix)
