import numpy as np
from scipy.optimize import curve_fit
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn


def build_QFT(N, regs):
    for i in range(N):
        circ.apply_gate('H', regs[i])                               
        for j in range(i + 1, N):
            theta = np.pi / 2 ** (j - i)     
            circ.apply_gate('CU1', theta, regs[i], regs[j])
                
    for i in range(N // 2):
        circ.apply_gate('SWAP', regs[i], regs[N - i - 1])


maxqubit = 5
ntimes = 10^2
nsampling = 10^2

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

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()


        build_QFT(N, regs)
        circ.sample(nsampling)


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

def f(x, a, b , c):
    return a * np.exp(b * x) + c

xaxis = np.arange(1, maxqubit + 1, 1)

popt, pcov = curve_fit(f, xaxis, meantotaltime)

plt.plot(xaxis, meantotaltime, 'bo', label='total time data')
plt.plot(xaxis, f(xaxis, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

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
#plt.savefig("~/QFT/QFT_TN_total_time_error.pdf")
plt.show()

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
#plt.savefig("~/QFT/QFT_TN_CPU_time_error.pdf")
plt.show()
