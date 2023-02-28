import quimb as qu
import quimb.tensor as qtn

# Number of qubits
N = 2

#create circuit
circ = qtn.Circuit(N)

for i in range(N)
    circ.apply_gate('H', regs[i])   #first we apply an Hadamard gate to the i-th qb

        for j in range(i + 1, N)
        circ.apply_gate('CU1', regs[i], regs[j])    #we apply a controlled unitary (1) gate to gate i and all gates below i
        
