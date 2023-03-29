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


maxqubit = 33       #33
nsampling = 10^5   #100k ?


for N in range(1, maxqubit + 1):
    regs = list(range(N))
    circ = qtn.Circuit(N)

    build_QFT(N, regs)

    bigmatrix = np.zeros((nsampling, N), np.int8)

    row = 0
    for b in circ.sample(nsampling):
        
        shot = list(b)
        bigmatrix[row] = shot
        row += 1

    farray = np.sum(bigmatrix, axis = 0) / nsampling

    rij = np.corrcoef(bigmatrix, rowvar= False)

    with open('/home/tommasogalletti/QFT/samples/TN__farrays.txt', mode='a') as file:
        np.savetxt(file, farray, delimiter=',')

    with open('/home/tommasogalletti/QFT/samples/TN__rs.txt', mode='a') as file:
        np.savetxt(file, rij, delimiter=',')



"""
circ.psi.draw(color=['H', 'CU1', 'SWAP'])                   #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths"""

# GUARDA PUBLICATION STYLE FIGURES - https://quimb.readthedocs.io/en/latest/tensor-drawing.html#publication-style-figures