import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

singletime = np.zeros(10)

maxqubit = 8
nsampling = 10**6

N = maxqubit

for i in range(10):

    circ = Circuit(N)
    for l in range(N):
        circ.add(gates.H(l))   
        for j in range(l + 1, N):
            theta = np.pi / 2 ** (j - l)    #rotation angle   
            circ.add(gates.CU1(l, j, theta= theta))
                    
    for l in range(N // 2):
        circ.add(gates.SWAP(l, N - l - 1))
    for l in range(N):
        circ.add(gates.M(l))


    ttot0 = timeit.default_timer()

    ######################
    result_state = circ(nshots = nsampling)
    samples = result_state.samples(binary=True)
    ######################

    ttot1 = timeit.default_timer()

    t = ttot1 - ttot0
    singletime[i] = t

print(' t = ')
print(np.mean(singletime))
print(' sigma = ')
print(np.std(singletime))
