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
            theta = np.pi / 2 ** (j - i)     
            circ.apply_gate('CU1', theta, regs[i], regs[j])
                
    for i in range(N // 2):
        circ.apply_gate('SWAP', regs[i], regs[N - i - 1])


maxqubit = 20       #33
nsampling = 10^5   #100k ?

for n in range(maxqubit):
    
    N = n + 1

    regs = list(range(N))
    circ = qtn.Circuit(N)

    build_QFT(N, regs)

    """for b in circ.sample(nsampling):         
            for a in range(maxqubit):
                bigmatrix[:,a] = b[a]"""

bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

for c in range(nsampling):    
    for a in range(maxqubit):       #serve questo for o si può fare in altro modo?
        for b in circ.sample(nsampling):       
            bigmatrix[c,a] = b[a]

farray = np.sum(bigmatrix, axis = 0) / nsampling

rij = np.corrcoef(bigmatrix, rowvar= False)

with open("TN_QFT_farray", 'w') as farray_file:
    for i in farray:
        np.savetxt(farray_file,i)

with open("TN_QFT_rij", 'w') as rij_file:
    for line in rij:
        np.savetxt(rij_file, line, fmt='%.2f')