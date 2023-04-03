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

singletime = np.zeros(10)

maxqubit = 8
nsampling = 1**6

N = maxqubit

for i in range(10):
    regs = list(range(N))
    circ = qtn.Circuit(N)
    build_QFT(N, regs)


    ttot0 = timeit.default_timer()

    ######################
    circ.sample(nsampling)
    ######################

    ttot1 = timeit.default_timer()

    t = ttot1 - ttot0
    singletime[i] = t

print(' t = ')
print(np.mean(singletime))
print(' sigma = ')
print(np.std(singletime))
