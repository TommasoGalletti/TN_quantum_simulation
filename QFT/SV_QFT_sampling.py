import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

maxqubit = 28       #28
nsampling = 10**4    #10k


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

    farray = np.sum(samples, axis = 0) / nsampling
    print(farray)

    rij = np.corrcoef(samples, rowvar= False)
    print(rij)

    with open('/home/tommasogalletti/QFT/samples/SV_farrays.csv', mode='a') as file:
        np.savetxt(file, farray.reshape(1, farray.shape[0]), delimiter=',',fmt="%f")

    with open('/home/tommasogalletti/QFT/samples/SV_rs.csv', mode='a') as file:
        if N > 1:
            for row in rij:
                np.savetxt(file, row.reshape(1, row.shape[0]), delimiter=',',fmt="%f", newline=",")
            file.write("\n")

circ.psi.draw(color=['H', 'CU1', 'SWAP'])                   #circuit drawing - focus on gate types
