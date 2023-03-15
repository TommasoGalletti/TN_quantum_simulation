import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import seaborn as sns

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


maxqubit = 6       #40
ntimes = 1000     #1000
nsampling = 1000   #100k ?

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

        shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence
        #print(f'Secret shift sequence: {shift}')
        build_HS(N, regs, shift)                   #circuit module

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

#print(bigmatrix)   

farray = np.sum(bigmatrix, axis = 0) / nsampling
#print(farray)

rij = np.corrcoef(bigmatrix, rowvar= False)
#print(rij)

#frequency histogram
histo = plt.bar(np.arange(maxqubit), farray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_frequency_histo.pdf")

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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_total_time_error.pdf")

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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_CPU_time_error.pdf")

#Correlation heatmap
mask = np.triu(np.ones_like(rij, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(rij, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit result correlation')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_correlation_heatmap.pdf")