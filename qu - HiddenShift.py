import numpy as np
import random

import quimb as qu
import quimb.tensor as qtn

N = 50

shift = [random.randint(0, 1) for _ in range(N)]  #create random shift sequence
print(f'Secret shift sequence: {shift}')

regs = list(range(N))

circ = qtn.Circuit(N)

"""def oracle(self):                                           #Implement function {f(x) = Σ_i x_(2i) x_(2i+1)} as a series of CZ gates
    for i in range(N // 2):                                 #oracle f
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])"""

#Hadamard (superposition - they act as a QFT)
for i in range(N):
    circ.apply_gate('H', regs[i])

for k in range(len(shift)):             #apply shift (|x> -> X|x>)
    if shift[k]:
        circ.apply_gate('X', regs[k])

for i in range(N // 2):                                 #query oracle f
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

for k in range(len(shift)):             #apply shift (recover |x> states)
    if shift[k]:
        circ.apply_gate('X', regs[k])

#Hadamard (fourier transform to generate superposition with an extra phase added to f(x+s))
for i in range(N):
    circ.apply_gate('H', regs[i])

for i in range(N // 2):                                 #query oracle f (this simplifies the phase)
        circ.apply_gate('CZ', regs[2*i], regs[2*i + 1])

#Hadamard (inverse fourier transform -> go back to the shift state |s>)
for i in range(N):
    circ.apply_gate('H', regs[i])


#MEASURE
results = list()
for b in circ.sample(20):   #20 samples
    print(b)
    results.append(b)

circ.psi.draw(color=['H', 'CZ', 'X'])                       #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths
   