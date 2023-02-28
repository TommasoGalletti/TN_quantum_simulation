import numpy as np
from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

# N qubits
N = 2

#omitted: initial state

#circuit
circuit = QFT(N)

#circuit execution
result = circuit(initial_state) 

#printing result state
print(result.state())