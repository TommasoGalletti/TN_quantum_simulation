import quimb as qu
import quimb.tensor as qtn
import numpy
import math

N = 2
circ = qtn.Circuit(N)

circ.apply_gate('H', 0)
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('RZ', 1.57, 1)

circ.apply_gate('RY', 2 * numpy.arccos(1 / math.sqrt(3)), 1)
#controlled Hadamard between 0, 1
circ.apply_gate('CNOT', 1, 2)
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('X', 0)             #PAULI X: NOT

gates = [
            ('CX', 0, 1, 3),
            ('CNOT', 0, 1),
            ('CX', 1, 2, 3),
            ('CNOT', 1, 2),
            ('CNOT', 0, 1)
        ]

circ.apply_gates(gates)

circ.apply_gate('ccX', 0, 1, 3) # <--- errore 
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('ccX', 1, 2, 3)
circ.apply_gate('CNOT', 1, 2)
circ.apply_gate('CNOT', 0, 1)

#circ.psi.draw(color=['CX', 'CNOT'])
#circ.psi.draw(color=['H', 'CNOT', 'RZ'])