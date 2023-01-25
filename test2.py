import quimb as qu
import quimb.tensor as qtn

n = 10
# 'n' qubits and tag the initial wavefunction tensors
circ = qtn.Circuit(N=n)

# initial layer of hadamards
for i in range(n):
    circ.apply_gate('H', i, gate_round=0)
    
# 8 rounds of entangling gates
for r in range(1, n-1):
    
    # even pairs
    for i in range(0, n, 2):
        circ.apply_gate('CNOT', i, i + 1, gate_round=r)

    # Y-rotations    
    for i in range(n):
        circ.apply_gate('RZ', 1.234, i, gate_round=r)

    # odd pairs
    for i in range(1, n-1, 2):
        circ.apply_gate('CZ', i, i + 1, gate_round=r)

    # X-rotations    
    for i in range(n):
        circ.apply_gate('RX', 1.234, i, gate_round=r)

# final layer of hadamards
for i in range(n):
    circ.apply_gate('H', i, gate_round=r + 1)

print(circ)

circ.psi.draw(color=['PSI0', 'H', 'CNOT', 'RZ', 'RX', 'CZ'])

circ.psi.draw(color=[f'I{i}' for i in range(n)])

circ.psi.draw(color=['PSI0'] + [f'ROUND_{i}' for i in range(n)])

print( circ.psi.select(['CNOT', 'I3', 'ROUND_3'], which='all'))
