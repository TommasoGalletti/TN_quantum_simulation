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

for n in range(maxqubit):

    N = n + 1

    circ = QFT(N)
    #result_state = circ()  #QUESTO?


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