import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

maxqubit = 2       #33
nsampling = 4    #100k ?

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

#sample = result_state.samples(binary=True)

print(result_state.samples(binary=True))
#print(sample)

bigmatrix = np.zeros((nsampling, maxqubit), np.int8)