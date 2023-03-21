import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#usage: python <TN vs SV> <TNfarray.txt> <TNRij.txt> <SVfarray.txt> <SVRij.txt>

#tnfarrayfile = 
#tnrijfile = 
#svfarrayfile = 
#svrijfile = 


maxqubit = 33

#TN data
tnfarray = np.loadtxt("TN_QFT_results")
tnrij = np.loadtxt("TN_QFT_rij", dtype= np.float32)

#SV data
svfarray = np.loadtxt("SV_QFT_results")
svrij = np.loadtxt("SV_QFT_rij", dtype= np.float32)

#distanza euclidea
fdist = np.linalg.norm(tnfarray - svfarray)

#pearson correlation (?)
pearsoncorr = np.corrcoef(tnfarray, svfarray)

#wilcoxon-mann-whitney test
#test di Kolmogorov-Smirnov
#test t di Student?


#Frobenius norm della matrice differenza
corrdist = np.linalg.norm(tnrij - svrij)



#TN frequency histogram
histo = plt.bar(np.arange(maxqubit), tnfarray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_frequency_histo.pdf")

#SV frequency histogram
histo = plt.bar(np.arange(maxqubit), svfarray)
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_frequency_histo.pdf")

#TN Correlation heatmap
mask = np.triu(np.ones_like(tnrij, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(tnrij, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - tensor network simulation')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_TN_correlation_heatmap.pdf")

#SV Correlation heatmap
mask = np.triu(np.ones_like(svrij, dtype=bool))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
f, ax = plt.subplots(figsize=(maxqubit,maxqubit))
heatmap = sns.heatmap(tnrij, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
f.suptitle('Qubit correlation - state-vector simulation')
f.supxlabel('Qubit #')
f.supylabel('Qubit #')
plt.legend('Cij = COV(X_i,X_j)/(VAR(X_i)*VAR(X_j))^0.5', loc="upper right")
plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/QFT/QFT_SV_correlation_heatmap.pdf")