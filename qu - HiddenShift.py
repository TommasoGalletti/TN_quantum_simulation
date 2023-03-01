import numpy as np

import quimb as qu
import quimb.tensor as qtn

N = 2

regs = list(range(N))

circ = qtn.Circuit(N)

def oracle(self):                                           #Implement function {f(x) = Σ_i x_(2i) x_(2i+1)}.
    for i in range(N // 2):
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

#Hadamard
for i in range(N):
    circ.apply_gate('H', regs[i])

for i, ish in enumerate(self.shift):    #cos'è self.shift?
    if ish:
        circ.apply_gate('X', regs[i])

for gate in self.oracle():              #che fa?
    circ.apply_gate('gate', )

for i, ish in enumerate(self.shift):    #cos'è self.shift?
    if ish:
        circ.apply_gate('X', regs[i])

#Hadamard
for i in range(N):
    circ.apply_gate('H', regs[i])

for gate in self.oracle():              #..?
    circ.apply_gate('gate', )

#Hadamard
for i in range(N):
    circ.apply_gate('H', regs[i])

#MEASURE
results = list()
for b in circ.sample(20):   #20 samples
    print(b)
    results.append(b)

