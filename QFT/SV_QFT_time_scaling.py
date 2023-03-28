import numpy as np
from scipy.optimize import curve_fit
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

from qibo.models import Circuit
from qibo import gates

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

        circ = Circuit(N)

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()


        for i in range(N):

            circ.add(gates.H(i))    
            for j in range(i + 1, N):
                theta = np.pi / 2 ** (j - i)    #rotation angle   
                circ.add(gates.CU1(i, j, theta= theta))
                        
        for i in range(N // 2):
            circ.add(gates.SWAP(i, N - i - 1))

        for i in range(N):
            circ.add(gates.M(i))

        result_state = circ(nshots = nsampling)
        samples = result_state.samples(binary=True)


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
fig2, ax2 = plt.figure()
x = np.arange(1, maxqubit + 1, 1)
y = meantotaltime
yerr = totaltimeerror
ax2.set_ylim(bottom= 0) #???
plt.errorbar(x, y, yerr=yerr)
fig2.suptitle('Total time')
fig2.supxlabel('# of qubits')
fig2.supylabel('time [s]')
#plt.legend(loc='upper left')
#plt.savefig("~/QFT/QFT_SV_total_time_error.pdf")
plt.show()

#CPU time
fig4, ax4 = plt.figure()
x = np.arange(1, maxqubit + 1, 1)
y = meanprocesstime
yerr = processtimeerror
ax4.set_ylim(bottom= 0) #???
plt.errorbar(x, y, yerr=yerr)
fig4.suptitle('CPU time')
fig4.supxlabel('# of qubits')
fig4.supylabel('time [s]')
#plt.legend(loc='upper left')
#plt.savefig("~/QFT/QFT_SV_CPU_time_error.pdf")
plt.show()
