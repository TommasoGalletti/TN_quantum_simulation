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
nsampling = 20   #100k ?
 
N = maxqubit

regs = list(range(N))
circ = qtn.Circuit(N)

build_QFT(N, regs)

"""for b in circ.sample(nsampling):         
        for a in range(maxqubit):
            bigmatrix[:,a] = b[a]"""

bigmatrix = np.zeros((nsampling, N), np.int8)

#CONTROLLA QUA - versione precedente a scambio la trovi commentata in SV_QFT
for c in range(nsampling):
    b = circ.sample()
    print(b)  
    for a in range(maxqubit):       
        bigmatrix[c,a] = b[a]
print(bigmatrix)

farray = np.sum(bigmatrix, axis = 0) / nsampling

rij = np.corrcoef(bigmatrix, rowvar= False)

with open("TN_QFT_farray", 'w') as farray_file:
    for i in farray:
        np.savetxt(farray_file,i)

with open("TN_QFT_rij", 'w') as rij_file:
    for line in rij:
        np.savetxt(rij_file, line, fmt='%.2f')

circ.psi.draw(color=['H', 'CU1', 'SWAP'])                   #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths

# GUARDA PUBLICATION STYLE FIGURES - https://quimb.readthedocs.io/en/latest/tensor-drawing.html#publication-style-figures