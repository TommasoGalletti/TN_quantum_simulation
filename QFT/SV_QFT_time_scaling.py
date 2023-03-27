import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

maxqubit = 1       #37  #######
ntimes = 1       #1000  #######
nsampling = 10          #######

meantotaltime = np.zeros(maxqubit, np.float32)
totaltimeerror = np.zeros(maxqubit, np.float32)
meanprocesstime = np.zeros(maxqubit, np.float32)
processtimeerror = np.zeros(maxqubit, np.float32)

for n in range(maxqubit):

    singletotaltime = np.zeros(ntimes, np.float32)
    singleprocesstime = np.zeros(ntimes, np.float32)

    N = n + 5   #########

    for i in range(ntimes):

        ttot0 = timeit.default_timer()
        tprocess0 = time.process_time()

    #########
        circ = QFT(N)
        for m in range(N):
            circ.add(gates.M(m, collapse= True))
    #########
        result_state = circ(nshots = nsampling)

        result_state.sample_to_binary()     #######
        result_state.saples(binary=True)    #######
        print(result_state) 

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

"""
meantotfit = np.polyfit(np.arange(maxqubit), np.log(meantotaltime), 1) #fatto in 5 sec controlla


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
plt.savefig("~/QFT/QFT_SV_total_time_error.pdf")

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
plt.savefig("~/QFT/QFT_SV_CPU_time_error.pdf")
"""