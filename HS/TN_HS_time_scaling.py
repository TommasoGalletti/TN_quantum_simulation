import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

import quimb as qu
import quimb.tensor as qtn


def build_HS(N, regs, shift):
    for i in range(N):                          #Hadamard (superposition - they act as a QFT)
        circ.apply_gate('H', regs[i])

    for k in range(len(shift)):                 #apply shift (|x> -> X|x>)
        if shift[k]:
            circ.apply_gate('X', regs[k])

    for i in range(N // 2):                     #query oracle f
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

    for k in range(len(shift)):                 #apply shift (recover |x> states)
        if shift[k]:
            circ.apply_gate('X', regs[k])

    for i in range(N):                          #Hadamard (fourier transform to generate superposition with an extra phase added to f(x+s))
        circ.apply_gate('H', regs[i])

    for i in range(N // 2):                     #query oracle f (this simplifies the phase)
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

    for i in range(N):                          #Hadamard (inverse fourier transform -> go back to the shift state |s>)
        circ.apply_gate('H', regs[i])



maxqubit = 28
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
        shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence

        build_HS(N, regs, shift)

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
    processtimeerror[n] = np.std(singleprocesstime)

np.savetxt('/home/tommasogalletti/HS/time_arrays/TN_times.csv', (meantotaltime, totaltimeerror, meanprocesstime, processtimeerror), delimiter=',')
