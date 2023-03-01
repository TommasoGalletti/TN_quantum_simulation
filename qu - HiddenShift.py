import numpy as np

import quimb as qu
import quimb.tensor as qtn

N = 2

regs = list(range(N))

circ = qtn.Circuit(N)

def oracle(self):                                           #Implement function {f(x) = Σ_i x_(2i) x_(2i+1)} as a series of CZ gates
    for i in range(N // 2):                                 #oracle f
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

#Hadamard (superposition - they act as a QFT)
for i in range(N):
    circ.apply_gate('H', regs[i])

for i, ish in enumerate(self.shift):    #apply shift (|x> -> X|x>)
    if ish:
        circ.apply_gate('X', regs[i])

for gate in self.oracle():              #query oracle f
        circ.apply_gate('gate', )

for i, ish in enumerate(self.shift):    #apply shift (recover the |x> states)
    if ish:
        circ.apply_gate('X', regs[i])

#Hadamard (fourier transform to generate superposition with an extra phase added to f(x+s))
for i in range(N):
    circ.apply_gate('H', regs[i])

for gate in self.oracle():              #query oracle f (this simplifies the phase)
    circ.apply_gate('gate', )

#Hadamard (inverse fourier transform -> go back to the shift state |s>)
for i in range(N):
    circ.apply_gate('H', regs[i])

#MEASURE
results = list()
for b in circ.sample(20):   #20 samples
    print(b)
    results.append(b)

