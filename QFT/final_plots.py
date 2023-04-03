import numpy as np
from scipy.optimize import curve_fit
import matplotlib as mpl
import matplotlib.pyplot as plt

maxqubit = 30
xaxis = np.arange(1, maxqubit + 1, 1)

tntimes = list()

with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/time_arrays/TN_finaltimes.csv") as fp:
    lines = fp.readlines()
    for l in lines:
        l.strip("\n")
        l = "[" + l + "]"
        tntimes.append(np.array(eval(l)))

tntot = tntimes[0]
tntot_err = tntimes[1]

def f(x, a, b , c):
    return a * np.exp(b * x) + c

popttntot, pcovtntot = curve_fit(f, xaxis, tntot)   #TN TOT

yerr = tntot_err
plt.errorbar(xaxis, tntot, yerr=yerr, fmt='yo', ecolor='lightgray', label=' TN total time')
#plt.plot(xaxis, f(xaxis, *popttntot), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popttntot))
plt.xlabel('# of qubits')
plt.ylabel('TN total time [s]')
plt.legend()
plt.title('TN QFT total execution time - parameters: ntimes = 10^2, nsample = 10^4')
plt.grid()
plt.show()
#plt.savefig("~/QFT/plots/QFT_TN_tot.pdf")
