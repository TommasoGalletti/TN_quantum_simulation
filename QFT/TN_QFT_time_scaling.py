import numpy as np
from scipy.optimize import curve_fit
import time
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


maxqubit = 33
ntimes = 10**2
nsampling = 10**4

meantotaltime = np.zeros(maxqubit, np.float32)
totaltimeerror = np.zeros(maxqubit, np.float32)
meanprocesstime = np.zeros(maxqubit, np.float32)
processtimeerror = np.zeros(maxqubit, np.float32)

for n in range(maxqubit):

    singletotaltime = np.zeros(ntimes, np.float32)
    singleprocesstime = np.zeros(ntimes, np.float32)

    N = n + 1

    for i in range(ntimes):

        regs = list(range(N))
        circ = qtn.Circuit(N)
        build_QFT(N, regs)

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time() 

        #####################
        circ.sample(nsampling)
        #####################

        ttot1 = timeit.default_timer()
        tprocess1 = time.process_time()

        ttot = ttot1 - ttot0
        tprocess = tprocess1 - tprocess0

        singletotaltime[i] = ttot
        singleprocesstime[i] = tprocess

    meantotaltime[n] = np.mean(singletotaltime)
    totaltimeerror[n] = np.std(singletotaltime)

    meanprocesstime[n] = np.mean(singleprocesstime)
    processtimeerror[n] = np.mean(singleprocesstime)

np.savetxt('/home/tommasogalletti/QFT/time_arrays/TN_times.csv', (meantotaltime, totaltimeerror, meanprocesstime, processtimeerror), delimiter=',')
