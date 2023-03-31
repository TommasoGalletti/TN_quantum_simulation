import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import quimb as qu
import quimb.tensor as qtn


def build_QFT(N, regs):
    for h in range(N):
        circ.apply_gate('H', regs[h])                               
        for j in range(h + 1, N):
            theta = np.pi / 2 ** (j - h)    #rotation angle   
            circ.apply_gate('CU1', theta, regs[h], regs[j])
                
    for s in range(N // 2):
        circ.apply_gate('SWAP', regs[s], regs[N - s - 1])


maxqubit = 28       #28
nsampling = 10**4   #10k ?


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

    if N > 1:
        rij = np.corrcoef(bigmatrix, rowvar= False)
        print(rij)

    with open('/home/tommasogalletti/QFT/samples/TN_farrays.csv', mode='a') as file:
        np.savetxt(file, farray.reshape(1, farray.shape[0]), delimiter=',',fmt="%f")

    with open('/home/tommasogalletti/QFT/samples/TN_rs.csv', mode='a') as file:
        if N > 1:
            for row in rij:
                np.savetxt(file, row.reshape(1, row.shape[0]), delimiter=',',fmt="%f", newline=",")
            file.write("\n")

"""
circ.psi.draw(color=['H', 'CU1', 'SWAP'])                   #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths

# GUARDA PUBLICATION STYLE FIGURES - https://quimb.readthedocs.io/en/latest/tensor-drawing.html#publication-style-figures
"""