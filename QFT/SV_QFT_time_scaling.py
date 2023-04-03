import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

from qibo.models import Circuit
from qibo import gates

maxqubit = 20
ntimes = 10**2
nsampling = 10**4

meantotaltime = np.zeros(maxqubit, np.float32)
totaltimeerror = np.zeros(maxqubit, np.float32)

for n in range(maxqubit):

    singletotaltime = np.zeros(ntimes, np.float32)

    N = n + 1

    for i in range(ntimes):

        circ = Circuit(N)

        ttot0 = timeit.default_timer()

        ###########################################
        for l in range(N):

            circ.add(gates.H(l))   
            for j in range(l + 1, N):

                theta = np.pi / 2 ** (j - l)    #rotation angle   
                circ.add(gates.CU1(l, j, theta= theta))
                        
        for l in range(N // 2):
            circ.add(gates.SWAP(l, N - l - 1))

        for l in range(N):
            circ.add(gates.M(l))

        result_state = circ(nshots = nsampling)
        samples = result_state.samples(binary=True)
        ###########################################

        ttot1 = timeit.default_timer()

        ttot = ttot1 - ttot0

        singletotaltime[i] = ttot

    meantotaltime[n] = np.mean(singletotaltime)
    totaltimeerror[n] = np.std(singletotaltime)

np.savetxt('/home/tommasogalletti/QFT/time_arrays/SV_times.csv', (meantotaltime, totaltimeerror), delimiter=',')
