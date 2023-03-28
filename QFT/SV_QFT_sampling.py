import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

maxqubit = 3       #33
nsampling = 8    #100k ?

N = maxqubit

circ = Circuit(N)
for i in range(N):

    circ.add(gates.H(i))    
    for j in range(i + 1, N):
        theta = np.pi / 2 ** (j - i)    #rotation angle   
        circ.add(gates.CU1(i, j, theta= theta))
                
for i in range(N // 2):
    circ.add(gates.SWAP(i, N - i - 1))

for i in range(N):
    circ.add(gates.M(i))


result_state = circ(nshots = nsampling)

samples = result_state.samples(binary=True)

"""
bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

row = 0
for s in samples:
    bigmatrix[row] = s
    row += 1

print(bigmatrix)"""   

farray = np.sum(samples, axis = 0) / nsampling
print(farray)

rij = np.corrcoef(samples, rowvar= False)
print(rij)

np.savetxt('SV_samples.txt', (farray, rij), delimiter=',')
