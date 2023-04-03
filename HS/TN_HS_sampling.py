import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import seaborn as sns

import quimb as qu
import quimb.tensor as qtn

maxqubit = 18       #30
nsampling = 100       #10k ?

#with open('/home/tommasogalletti/HS/samples/TN_counters.csv', mode='a') as file:     #c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation
    #file.write("nsampling = " + str(nsampling) + "\n")

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

counter = np.zeros(maxqubit, dtype= np.int32)

for N in range(1, maxqubit + 1):
    regs = list(range(N))
    circ = qtn.Circuit(N)

    shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence

    build_HS(N, regs, shift= shift)


    for b in circ.sample(nsampling):
        shot = list(map(int, b))
        if(shot == shift):
            counter[N - 1] += 1
        
#with open('/home/tommasogalletti/HS/samples/TN_counters.csv', mode='a') as file:
    #np.savetxt(file, counter.reshape(1, counter.shape[0]), delimiter=',',fmt="%i")

circ.psi.draw(color=['H', 'CZ', 'X'])                   #circuit drawing - focus on gate types
