import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn

maxqubit = 40
ntimes = 1000
nsampling = 10**5

meantotaltime = list()
meanprocesstime = list()

for n in range(maxqubit):
    
    ttot = 0
    tprocess = 0

    for i in range(ntimes):
        N = n + 1

        regs = list(range(N))
        circ = qtn.Circuit(N)

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()

        for i in range(N):
            circ.apply_gate('H', regs[i])                               #first we apply an Hadamard gate to the i-th qb

            for j in range(i + 1, N):
                theta = np.pi / 2 ** (j - i)                            #calculating theta angle, which we feed as a parameter to the CU1 gate
                circ.apply_gate('CU1', theta, regs[i], regs[j])         #we apply a controlled unitary (1) gate to gate i and all gates below i
                
        for i in range(N // 2):
            circ.apply_gate('SWAP', regs[i], regs[N - i - 1])           #swap gates

        ttot1 = timeit.default_timer()
        tprocess1 = time.process_time()

        ttot += ttot1 - ttot0
        tprocess += tprocess1 - tprocess0
    
    meantotaltime.append(ttot / ntimes)
    meanprocesstime.append(tprocess / ntimes)

        