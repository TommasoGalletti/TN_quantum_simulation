import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sys  #robe da riga di comando

maxqubit = 33


sv_data = np.loadtxt('SV_samples.txt', delimiter=',')
sv_farray = sv_data[0]
sv_r = sv_data[1:]

tn_data = np.loadtxt('TN_samples.txt', delimiter=',')
tn_farray = tn_data[0]
tn_r = tn_data[1:]


#distanza euclidea
fdist = np.linalg.norm(tn_farray - sv_farray)

#pearson correlation (?)
pearsoncorr = np.corrcoef(tn_farray, sv_farray)

#wilcoxon-mann-whitney test
#test di Kolmogorov-Smirnov
#test t di Student?


#Frobenius norm della matrice differenza
corrdist = np.linalg.norm(tn_r - sv_r)



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
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_correlation_heatmap.pdf")
