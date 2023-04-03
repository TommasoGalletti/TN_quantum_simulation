import numpy as np
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn

def build_QFT(N, regs):
    for h in range(N):
        circ.apply_gate('H', regs[h])                               
        for j in range(h + 1, N):
            theta = np.pi / 2 ** (j - h)     
            circ.apply_gate('CU1', theta, regs[h], regs[j])
                
    for s in range(N // 2):
        circ.apply_gate('SWAP', regs[s], regs[N - s - 1])


maxqubit = 30
ntimes = 100
nsampling = 10000

meantotaltime = np.zeros(maxqubit, np.float32)
totaltimeerror = np.zeros(maxqubit, np.float32)

for n in range(maxqubit):

    singletotaltime = np.zeros(ntimes, np.float32)

    N = n + 1

    for t in range(ntimes):

        regs = list(range(N))
        circ = qtn.Circuit(N)
        

        ttot0 = timeit.default_timer()

        ######################
        build_QFT(N, regs)
        circ.sample(nsampling)
        ######################

        ttot1 = timeit.default_timer()

        ttot = ttot1 - ttot0

        singletotaltime[t] = ttot

    meantotaltime[n] = np.mean(singletotaltime)
    totaltimeerror[n] = np.std(singletotaltime)

np.savetxt('c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/time_arrays/test.csv', (meantotaltime, totaltimeerror), delimiter=',')
