import numpy as np
from qibo.models import Circuit
from qibo import gates

# Construct the circuit
c = Circuit(2)

# Add some gates
c.add(gates.H(0))
c.add(gates.H(1))

# Define an initial state (optional - default initial state is |00>)
initial_state = np.ones(4) / 2.0

# Execute the circuit and obtain the final state
result = c(initial_state) # c.execute(initial_state) also works
print(result.state())

# should print `tf.Tensor([1, 0, 0, 0])`
print(result.state(numpy=True))

# should print `np.array([1, 0, 0, 0])`
