import argparse

import numpy as np

import quimb as qu
import quimb.tensor as qtn

from qibo import hamiltonians, models

nqubits = 4
layers = 2
maxsteps = 5000
T_max = 4

regs = list(range(nqubits))

circ = qtn.Circuit(nqubits)

for l in range(layers):
    for q in range(nqubits):              circ.apply_gate('RY', 0, regs[q])
    for q in range(0, nqubits - 1, 2):    circ.apply_gate('CZ', regs[q], regs[q+1])
    for q in range(nqubits):              circ.apply_gate('RY', 0, regs[q])
    for q in range(0, nqubits - 1, 2):    circ.apply_gate('CZ', regs[q], regs[q+1])
    circ.apply_gate('CZ', regs[0], regs[nqubits - 1])

for q in range(nqubits):
    circ.apply_gate('RY', 0, regs[q])

problem_hamiltonian = hamiltonians.XXZ(nqubits)
easy_hamiltonian = hamiltonians.X(nqubits)

s = lambda t: t
aavqe = models.variational.AAVQE(circ, easy_hamiltonian, problem_hamiltonian, s, nsteps=maxsteps, t_max=T_max)

initial_parameters = np.random.uniform( 0, 2 * np.pi * 0.1, 2 * nqubits * layers + nqubits)
best, params = aavqe.minimize(initial_parameters)

print("Final parameters: ", params)
print("Final energy: ", best)

# We compute the difference from the exact value to check performance
eigenvalue = problem_hamiltonian.eigenvalues()
print(eigenvalue)
print("Difference from exact value: ", best - np.real(eigenvalue[0]))
print("Log difference: ", -np.log10(best - np.real(eigenvalue[0])))


"""results = list()
for b in circ.sample(20):   #20 samples
    print(b)
    results.append(b)"""

circ.psi.draw(color=['H', 'CZ', 'X'])                       #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(nqubits)])      #circuit drawing - focus on qubit paths 