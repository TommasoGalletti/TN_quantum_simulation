import numpy as np
from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

maxqubit = 33
N = maxqubit
nsampling = 10^5

#segnarsi scaling di tempo anche per Qibo

#omitted: initial_state (default is |0>^N)

#circuit
circuit = QFT(N)

#circuit execution
result = circuit()


bigmatrix = np.zeros((nsampling, maxqubit), np.int8)

#printing result state
print(result.state())