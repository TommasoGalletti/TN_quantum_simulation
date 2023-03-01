import numpy as np
import random

import quimb as qu
import quimb.tensor as qtn

N = 3

regs = list(range(N))

circ = qtn.Circuit(N)

circ.apply_gate('X', regs[N-1])

for i in range(N):
    circ.apply_gate('H', regs[i])

for i in range(N - 1):
        circ.apply_gate('CNOT', regs[i], regs[N-1])

for i in range(N - 1):
        circ.apply_gate('H', regs[i])

results = list()
for b in circ.sample(20):   #20 samples
    print(b)
    results.append(b)

circ.psi.draw(color=['H', 'CNOT', 'X'])                       #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths
