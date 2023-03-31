import numpy as np
from scipy.optimize import curve_fit
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

from qibo.models import Circuit
from qibo import gates

maxqubit = 3
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
        tprocess0 = time.process_time()

        ###########################################
        result_state = circ(nshots = nsampling)
        samples = result_state.samples(binary=True)
        ###########################################

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

np.savetxt('/home/tommasogalletti/QFT/time_arrays/SV_times.csv', (meantotaltime, totaltimeerror, meanprocesstime, processtimeerror), delimiter=',')
