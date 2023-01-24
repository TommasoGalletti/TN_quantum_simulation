import quimb as qu
import quimb.tensor as qtn
import numpy
import math

N = 3
circ = qtn.Circuit(N)

circ.apply_gate('RY', 2 * numpy.arccos(1 / math.sqrt(3)), 1)
#controlled Hadamard between 0, 1
circ.apply_gate('CNOT', 1, 2)
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('X', 0)             #PAULI X: NOT


circ.psi.draw(color=['H', 'CNOT'])