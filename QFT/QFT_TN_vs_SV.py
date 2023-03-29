import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sys  #robe da riga di comando

maxqubit = 33

tnfarrays = []
tnrijs = []

with open('/TN_samples.txt', mode='r') as file:
    for line in file:
        line = line.strip()  # remove leading/trailing white space
        if not line:         # skip empty lines
            continue
        # split line into farray and rij using comma as delimiter
        farray, rij = line.split(',')
        # convert farray and rij strings to numpy arrays
        farray = np.fromstring(farray, sep=',')
        rij = np.fromstring(rij, sep=',').reshape((len(farray), len(farray)))
        # add farray and rij to respective lists
        tnfarrays.append(farray)
        tnrijs.append(rij)

svfarrays = []
svrijs = []

with open('/SV_samples.txt', mode='r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        farray, rij = line.split(',')

        farray = np.fromstring(farray, sep=',')
        rij = np.fromstring(rij, sep=',').reshape((len(farray), len(farray)))

        svfarrays.append(farray)
        svrijs.append(rij)



"""
sv_data = np.loadtxt('SV_samples.txt', delimiter=',')
sv_farray = sv_data[0]
sv_r = sv_data[1:]

tn_data = np.loadtxt('TN_samples.txt', delimiter=',')
tn_farray = tn_data[0]
tn_r = tn_data[1:]"""


#distanza euclidea - SI
fdist = np.zeros(maxqubit, np.float64)
for d in range(maxqubit):
    fdist[d] = np.linalg.norm(tnfarrays[d] - svfarrays[d])

#pearson correlation - NO
pearsoncorr = np.zeros(maxqubit, np.float64)
for p in range(maxqubit):
    pearsoncorr[p] = np.corrcoef(tnfarrays[p], svfarrays[p])


#wilcoxon-mann-whitney test
#test di Kolmogorov-Smirnov
#test t di Student?

#coefficiente di correlazione di Spearman o Kendall


#Frobenius norm della matrice differenza
corrdist = np.zeros(maxqubit, np.float64)
for d in range(maxqubit):
    corrdist[d] = np.linalg.norm(tnrijs[d] - svrijs[d])


"""
#TN frequency histogram
histo = plt.bar(np.arange(maxqubit), tn_farray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_frequency_histo.pdf")

#SV frequency histogram
histo = plt.bar(np.arange(maxqubit), sv_farray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_frequency_histo.pdf")

#TN Correlation heatmap
mask = np.triu(np.ones_like(tn_r, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(tn_r, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - tensor network simulation')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_correlation_heatmap.pdf")

#SV Correlation heatmap
mask = np.triu(np.ones_like(sv_r, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(tn_r, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - state-vector simulation')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_correlation_heatmap.pdf")"""
