import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn

maxqubit = 12       #40
ntimes = 1000       #1000
nsampling = 10**5   #100k ?

meantotaltime = list()
totaltimeerror = list()
meanprocesstime = list()
processtimeerror = list()

for n in range(maxqubit):

    singletotaltime = list()
    singleprocesstime = list()

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

        ttot = ttot1 - ttot0
        tprocess = tprocess1 - tprocess0

        singletotaltime.append(ttot)
        singleprocesstime.append(tprocess)

    
    meantotaltime.append(np.mean(singletotaltime))
    totaltimeerror.append(np.std(singletotaltime))

    meanprocesstime.append(np.mean(singleprocesstime))
    processtimeerror.append(np.std(singleprocesstime))

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