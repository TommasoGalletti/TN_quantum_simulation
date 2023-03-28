import numpy as np

rij = [[0.3, 0.2], [0.4, 0.8]]

with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/TN_QFT_farray.txt", 'w') as rij_file:
    for line in rij:
        np.savetxt(rij_file, line, fmt='%.2f')   #capire come funzione format)

np.fromfile()