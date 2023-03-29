import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

maxqubit = 33       #33
nsampling = 10^5    #100k ?


for N in range(1, maxqubit + 1):

    circ = Circuit(N)

    for i in range(N):

        circ.add(gates.H(i))    
        for j in range(i + 1, N):
            theta = np.pi / 2 ** (j - i)    #rotation angle   
            circ.add(gates.CU1(i, j, theta= theta))
                    
    for s in range(N // 2):
        circ.add(gates.SWAP(s, N - s - 1))

    for m in range(N):
        circ.add(gates.M(m))


    result_state = circ(nshots = nsampling)

    samples = result_state.samples(binary=True)

    """
    bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

    row = 0
    for s in samples:
        bigmatrix[row] = s
        row += 1

    print(bigmatrix)"""   

    farray = np.sum(samples, axis = 0) / nsampling
    print(farray)

    rij = np.corrcoef(samples, rowvar= False)
    print(rij)

    with open('/home/tommasogalletti/QFT/samples/SV__farrays.txt', mode='a') as file:
        np.savetxt(file, farray, delimiter=',')

    with open('/home/tommasogalletti/QFT/samples/SV__rs.txt', mode='a') as file:
        np.savetxt(file, rij, delimiter=',')