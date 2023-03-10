import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn

def build_QFT(N, regs):
    for i in range(N):
        circ.apply_gate('H', regs[i])                               #first we apply an Hadamard gate to the i-th qb

    for j in range(i + 1, N):
        theta = np.pi / 2 ** (j - i)                                #calculating theta angle, which we feed as a parameter to the CU1 gate
        circ.apply_gate('CU1', theta, regs[i], regs[j])             #we apply a controlled unitary (1) gate to gate i and all gates below i
                
    for i in range(N // 2):
        circ.apply_gate('SWAP', regs[i], regs[N - i - 1])           #swap gates


maxqubit = 3       #40
ntimes = 100       #1000
nsampling = 10   #100k ?

meantotaltime = np.zeros(maxqubit, np.float32)
totaltimeerror = np.zeros(maxqubit, np.float32)
meanprocesstime = np.zeros(maxqubit, np.float32)
processtimeerror = np.zeros(maxqubit, np.float32)

for n in range(maxqubit):

    singletotaltime = np.zeros(ntimes, np.float32)
    singleprocesstime = np.zeros(ntimes, np.float32)

    for i in range(ntimes):
        N = n + 1

        regs = list(range(N))
        circ = qtn.Circuit(N)

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()

        build_QFT(N, regs)

        ttot1 = timeit.default_timer()
        tprocess1 = time.process_time()

        ttot = ttot1 - ttot0
        tprocess = tprocess1 - tprocess0

        singletotaltime[i] = ttot
        singleprocesstime[i] = tprocess

    bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

    """for b in circ.sample(nsampling):         #print (sample string)_N_qbmax_1
            for a in range(maxqubit):
                bigmatrix[:,a] = b[a]"""

    meantotaltime[n] = np.mean(singletotaltime)
    totaltimeerror[n] = np.std(singletotaltime)

    meanprocesstime[n] = np.mean(singleprocesstime)
    processtimeerror[n] = np.mean(singleprocesstime)

for b in circ.sample(nsampling):        #print (sample string)_N_qbmax_1
        print(b)                        #2
        for a in range(maxqubit):       #3
            bigmatrix[:,a] = b[a]

        print(bigmatrix[n,:])

#total time
fig2 = plt.figure()
x = np.arange(1, maxqubit + 1, 1)
y = meantotaltime
yerr = totaltimeerror
plt.errorbar(x, y, yerr=yerr)
fig2.suptitle('Total time')
fig2.supxlabel('# of qubits')
fig2.supylabel('time [s]')
#plt.legend(loc='upper left')

plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_total_time_error.pdf")

#CPU time
fig4 = plt.figure()
x = np.arange(1, maxqubit + 1, 1)
y = meanprocesstime
yerr = processtimeerror
plt.errorbar(x, y, yerr=yerr)
fig4.suptitle('CPU time')
fig4.supxlabel('# of qubits')
fig4.supylabel('time [s]')
#plt.legend(loc='upper left')

plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_CPU_time_error.pdf")