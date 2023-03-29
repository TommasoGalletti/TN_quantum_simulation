import quimb as qu

# Costruisco un circuito tensoriale
qc = qu.TensorNetwork()
qc.apply_gate(qubit_gate_1, [0])
qc.apply_gate(qubit_gate_2, [1])
# etc.

# Calcolo lo stato finale
state = qc.to_dense()

# Ottengo la matrice densità
density_matrix = qu.outer(state, state.conj())

import numpy as np
from qibo.models import Circuit

# Costruisco un circuito
circuit = Circuit(n_qubits)
circuit.apply(qubit_gate_1, target=0)
circuit.apply(qubit_gate_2, target=1)
# etc.

# Calcolo lo stato finale
state_vector = circuit.execute()

# Ottengo la matrice densità
density_matrix = np.outer(state_vector, np.conj(state_vector).T)