import quimb as qu
import quimb.tensor as qtn

# Number of qubits
N = 2

#registro ordine qubit
regs = list(range(N))

#create circuit
circ = qtn.Circuit(N)

for i in range(N):
    circ.apply_gate('H', regs[i])                       #first we apply an Hadamard gate to the i-th qb

    for j in range(i + 1, N):
        circ.apply_gate('CU1', regs[i], regs[j])        #we apply a controlled unitary (1) gate to gate i and all gates below i
        
for i in range(N // 2):
    circ.apply_gate('SWAP', regs[i], regs[N - i - 1])   #swap gates



circ.psi.draw(color=['H', 'CU1', 'SWAP'])               #circuit drawing



for b in circ.sample(3):                                #sample results (3 times)
    print(b)

circ.amplitude('00')                                    #compute c = <x|U|psi0> (x = 00, U circuit, psi0 initial state)