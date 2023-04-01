import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sys  #robe da riga di comando

maxqubit = 28

tnfarrays = list()  #length = maxqubit        
tnrijs = list()     #lenght = maxqubit - 1
svfarrays = list()  #length = maxqubit
svrijs = list()     #lenght = maxqubit - 1
xaxis = np.arange(1, maxqubit + 1, 1)

#TN f arrays
with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/samples/TN_farrays.csv") as fp:
    lines = fp.readlines()
    for l in lines:
        l.strip("\n")
        l = "[" + l + "]"
        tnfarrays.append(np.array(eval(l)))

#TN corr matrices
with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/samples/TN_rs.csv") as fp:
    lines = fp.readlines()
    for row, l in enumerate(lines):
        l.strip("\n")
        l = "[" + l + "]"
        tnrijs.append(np.array(eval(l)).reshape(row+2, row+2))

#SV f arrays
with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/samples/SV_farrays.csv") as fp:
    lines = fp.readlines()
    for l in lines:
        l.strip("\n")
        l = "[" + l + "]"
        svfarrays.append(np.array(eval(l)))

#SV corr matrices
with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/samples/SV_rs.csv") as fp:
    lines = fp.readlines()
    for row, l in enumerate(lines):
        l.strip("\n")
        l = "[" + l + "]"
        svrijs.append(np.array(eval(l)).reshape(row+2, row+2))


#distanza euclidea - SI
fdist = np.zeros(maxqubit, np.float64)
for d in range(maxqubit):
    fdist[d] = np.linalg.norm(tnfarrays[d] - svfarrays[d])

normalized_fdist = np.zeros(maxqubit, np.float64)
for d in range(maxqubit):
    normalized_fdist[d] = fdist[d]/ np.linalg.norm(svfarrays[d])

fdist_per_qb = np.zeros(maxqubit, np.float64)
for d in range(maxqubit):
    fdist_per_qb[d] = fdist[d]/ (d + 1)

plt.plot(xaxis, fdist, 'g--')
plt.xlabel('# of qubits')
plt.ylabel('l^2 norm(tnfarrays - svfarrays)')
plt.ylim(0, 0.1)
#plt.legend()
plt.show()

plt.plot(xaxis, normalized_fdist, 'r--')
plt.xlabel('# of qubits')
plt.ylabel('l^2_norm(tnfarrays - svfarrays) / l^2_norm(svfarrays)')
plt.ylim(0, 0.1)
#plt.legend()
plt.show()

plt.plot(xaxis, fdist_per_qb, 'g--')
plt.xlabel('# of qubits')
plt.ylabel('l^2 norm(tnfarrays - svfarrays)/ # of qb')
plt.ylim(0, 0.1)
#plt.legend()
plt.show()

#Frobenius norm della matrice differenza
corrdist = np.zeros(maxqubit - 1, np.float64)
for d in range(maxqubit - 1):
    corrdist[d] = np.linalg.norm(tnrijs[d] - svrijs[d])

plt.plot(np.arange(2, maxqubit + 1, 1), corrdist, 'b--')
plt.xlabel('# of qubits')
plt.ylabel('l^2 norm(tnrs - svrs)')
plt.legend()
plt.show()

"""
#pearson correlation - NO
pearsoncorr = np.zeros(maxqubit, np.float64)
for p in range(maxqubit):
    pearsoncorr[p] = np.corrcoef(tnfarrays[p], svfarrays[p])


#wilcoxon-mann-whitney test
#test di Kolmogorov-Smirnov
#test t di Student?

#coefficiente di correlazione di Spearman


#TN frequency histogram
histo = plt.bar(np.arange(maxqubit), tn_farray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_frequency_histo.pdf")

#SV frequency histogram
histo = plt.bar(np.arange(maxqubit), sv_farray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_frequency_histo.pdf")
"""

"""
#TN Correlation heatmap (28 qubits) - tnrijs[maxqubit - 2]
#mask = np.triu(np.ones_like(tnrijs[maxqubit - 2], dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(tnrijs[maxqubit - 2], cmap=cmap, vmax=.3, center=0,       #mask=mask
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - tensor network simulation - 28 qubits')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
#plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_correlation_heatmap.pdf")
#plt.show()

#SV Correlation heatmap (28 qubits) - svrijs[maxqubit - 2]
#mask = np.triu(np.ones_like(svrijs[maxqubit - 2], dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(svrijs[maxqubit - 2], cmap=cmap, vmax=.3, center=0,      #mask=mask
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - state-vector simulation - 28 qubits')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
#plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_correlation_heatmap.pdf")
#plt.show()
"""
