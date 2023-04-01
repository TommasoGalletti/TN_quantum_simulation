import numpy as np
import random
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

from qibo.models import Circuit
from qibo import gates

maxqubit = 22
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
        shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence


        for i in range(N):                          #Hadamard (superposition - they act as a QFT)
            circ.add(gates.H(i))

        for k in range(len(shift)):                 #apply shift (|x> -> X|x>)
            if shift[k]:
                circ.add(gates.X(k))

        for z in range(N // 2):                     #query oracle f
            circ.add(gates.CZ(2*z, 2*z+1))

        for k in range(len(shift)):                 #apply shift (recover |x> states)
            if shift[k]:
                circ.add(gates.X(k))

        for h in range(N):                          #Hadamard (fourier transform to generate superposition with an extra phase added to f(x+s))
            circ.add(gates.H(h))

        for i in range(N // 2):                     #query oracle f (this simplifies the phase)
            circ.add(gates.CZ(2*i, 2*i + 1))

        for i in range(N):                          #Hadamard (inverse fourier transform -> go back to the shift state |s>)
            circ.add(gates.H(i))

        for m in range(N):
            circ.add(gates.M(m))


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
    processtimeerror[n] = np.std(singleprocesstime)

np.savetxt('/home/tommasogalletti/HS/time_arrays/SV_times.csv', (meantotaltime, totaltimeerror, meanprocesstime, processtimeerror), delimiter=',')
