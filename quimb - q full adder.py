import quimb as qu
import quimb.tensor as qtn

N = 4
circ = qtn.Circuit(N)

circ.apply_gate('ccX', 0, 1, 3) # <--- errore 
circ.apply_gate('CNOT', 0, 1)
circ.apply_gate('ccX', 1, 2, 3)
circ.apply_gate('CNOT', 1, 2)
circ.apply_gate('CNOT', 0, 1)

circ.psy.draw(color=['ccX', 'CNOT'])