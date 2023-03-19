import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

maxqubit = 20       #33
ntimes = 10^3     #1000
nsampling = 10^5   #100k ?

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

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()

        circ = QFT(N)
        #result_state = circ()  #QUESTO?

        ttot1 = timeit.default_timer()
        tprocess1 = time.process_time()

        ttot = ttot1 - ttot0
        tprocess = tprocess1 - tprocess0

        singletotaltime[i] = ttot
        singleprocesstime[i] = tprocess

    """for b in circ.sample(nsampling):         #print (sample string)_N_qbmax_1
            for a in range(maxqubit):
                bigmatrix[:,a] = b[a]"""

    meantotaltime[n] = np.mean(singletotaltime)
    totaltimeerror[n] = np.std(singletotaltime)

    meanprocesstime[n] = np.mean(singleprocesstime)
    processtimeerror[n] = np.mean(singleprocesstime)

bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

for c in range(nsampling):    
    for a in range(maxqubit):       #serve questo for o si può fare in altro modo?
        for b in circ.sample(nsampling):       
            bigmatrix[c,a] = b[a]


farray = np.sum(bigmatrix, axis = 0) / nsampling

rij = np.corrcoef(bigmatrix, rowvar= False)

with open("SV_QFT_farray", 'w') as farray_file:
    for i in farray:
        np.savetxt(farray_file,i)

with open("SV_QFT_rij", 'w') as rij_file:
    for line in rij:
        np.savetxt(rij_file, line, fmt='%.2f')

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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/SV_QFT_total_time_error.pdf")

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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/SV_QFT_CPU_time_error.pdf")