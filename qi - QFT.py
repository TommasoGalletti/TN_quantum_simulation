import numpy as np
from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

# N qubits
N = 37

#omitted: initial_state (default is |0>^N)

#circuit
circuit = QFT(N)

#circuit execution
result = circuit()

#printing result state
print(result.state())