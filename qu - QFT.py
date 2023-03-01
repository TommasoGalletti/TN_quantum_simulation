import numpy as np                  #FA TUTTO QUELLO CHE DEVE, FORSE PROBLEMA CON SWAPs

import quimb as qu
import quimb.tensor as qtn

# Number of qubits
N = 80                                                          #tested up to 80 qubits 

#registro ordine qubit
regs = list(range(N))

#create circuit
circ = qtn.Circuit(N)

for i in range(N):
    circ.apply_gate('H', regs[i])                               #first we apply an Hadamard gate to the i-th qb

    for j in range(i + 1, N):
        theta = np.pi / 2 ** (j - i)                            #calculating theta angle, which we feed as a parameter to the CU1 gate
        circ.apply_gate('CU1', theta, regs[i], regs[j])         #we apply a controlled unitary (1) gate to gate i and all gates below i
        
for i in range(N // 2):
    circ.apply_gate('SWAP', regs[i], regs[N - i - 1])           #swap gates

for b in circ.sample(3):                                        #sample results (3 times)
    print(b)

circ.psi.draw(color=['H', 'CU1', 'SWAP'])                       #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])                #circuit drawing - focus on qubit paths


#for b in range(2**N):
#print("x = 000, c = <x|U|psi0> = ", circ.amplitude('000'))           #compute c = <x|U|psi0> (x = 00, U circuit, psi0 initial state)