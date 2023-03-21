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


maxqubit = 4       #37
nsampling = 100       #100k ?

N = maxqubit    

regs = list(range(N))
circ = qtn.Circuit(N)


shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence
#print(f'Secret shift sequence: {shift}')
build_HS(N, regs, shift)                   #circuit module


bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

for c in range(nsampling):

    for b in circ.sample(1):        #QUA!
        print(b)
      
    for a in range(maxqubit):       
        bigmatrix[c,a] = b[a]

print(bigmatrix)

farray = np.sum(bigmatrix, axis = 0) / nsampling

rij = np.corrcoef(bigmatrix, rowvar= False)

"""#frequency histogram
histo = plt.bar(farray, width= np.arange(maxqubit))
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_frequency_histo.pdf")

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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/HS/HS_correlation_heatmap.pdf")"""
