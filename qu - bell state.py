import quimb as qu
import quimb.tensor as qtn

N = 2
circ = qtn.Circuit(N)

circ.apply_gate('H', 0)
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('RZ', 1.57, 1)

circ.psi.draw(color=['H', 'CNOT', 'RZ'])