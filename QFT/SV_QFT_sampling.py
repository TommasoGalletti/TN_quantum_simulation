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
nsampling = 10^5    #100k ?

N = maxqubit

circ = QFT(N)
#result_state = circ()  #QUESTO?

bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

#QUI VERSIONE PRECEDENTE A SCAMBIO DI FOR
#for c in range(nsampling):    
    #for a in range(maxqubit):
        #for b in circ.sample(nsampling):       
            #bigmatrix[c,a] = b[a]

for c in range(nsampling):
    result = circ()
    for a in range(maxqubit):
        bigmatrix[c,a] = result[a]

farray = np.sum(bigmatrix, axis = 0) / nsampling

rij = np.corrcoef(bigmatrix, rowvar= False)

with open("SV_QFT_farray", 'w') as farray_file:
    for i in farray:
        np.savetxt(farray_file,i)

with open("SV_QFT_rij", 'w') as rij_file:
    for line in rij:
        np.savetxt(rij_file, line, fmt='%.2f')