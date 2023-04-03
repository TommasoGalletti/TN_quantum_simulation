import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import seaborn as sns

from qibo.models import Circuit
from qibo import gates

maxqubit = 20       #30
nsampling = 100      #10k

with open('C:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/HS/samples/SV_counters.csv', mode='a') as file:     #c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation
    file.write("nsampling = " + str(nsampling) + "\n")

counter = np.zeros(maxqubit, dtype= np.int32)

for N in range(1, maxqubit + 1):
    circ = Circuit(N)

    shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence

    for i in range(N):                          #Hadamard (superposition - they act as a QFT)
        circ.add(gates.H(i))

    for k in range(len(shift)):                 #apply shift (|x> -> X|x>)
        if shift[k]:
            circ.add(gates.X(k))

    for z in range(N // 2):                     #query oracle f
        circ.add(gates.CZ(2*z, 2*z+1))

    for k in range(len(shift)):                 #apply shift (recover |x> states)
        if shift[k]:
            circ.add(gates.X(k))

    for h in range(N):                          #Hadamard (fourier transform to generate superposition with an extra phase added to f(x+s))
        circ.add(gates.H(h))

    for i in range(N // 2):                     #query oracle f (this simplifies the phase)
        circ.add(gates.CZ(2*i, 2*i + 1))

    for i in range(N):                          #Hadamard (inverse fourier transform -> go back to the shift state |s>)
        circ.add(gates.H(i))

    for m in range(N):
        circ.add(gates.M(m))

    result_state = circ(nshots = nsampling)

    samples = result_state.samples(binary=True)

    for line in samples:
        shot = list(line)
        if(shot == shift):
            counter[N - 1] += 1
        
with open('/home/tommasogalletti/HS/samples/SV_counters.csv', mode='a') as file:
    np.savetxt(file, counter.reshape(1, counter.shape[0]), delimiter=',',fmt="%i")
