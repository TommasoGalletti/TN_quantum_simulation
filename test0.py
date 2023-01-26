import quimb as qu
import quimb.tensor as qtn

print(sorted(qtn.circuit.ALL_GATES))

# STABLE 1.4.2
# ['CNOT', 'CU1', 'CU2', 'CU3', 'CX', 'CY', 'CZ', 'FS', 'FSIM', 'FSIMG', 'H', 'HZ_1_2', 'IDEN', 'IS', 'ISWAP', 'RX', 'RY', 'RZ', 'RZZ', 'S', 'SU4', 'SWAP', 'T', 'U1', 'U2', 'U3', 'W_1_2', 'X', 'X_1_2', 'Y', 'Y_1_2', 'Z', 'Z_1_2']

# DEV 1.4.3
# ['CNOT', 'CU1', 'CU2', 'CU3', 'CX', 'CY', 'CZ', 'FS', 'FSIM', 'FSIMG', 'H', 'HZ_1_2', 'IDEN', 'IS', 'ISWAP', 'RX', 'RY', 'RZ', 'RZZ', 'S', 'SU4', 'SWAP', 'T', 'U1', 'U2', 'U3', 'W_1_2', 'X', 'X_1_2', 'Y', 'Y_1_2', 'Z', 'Z_1_2']
