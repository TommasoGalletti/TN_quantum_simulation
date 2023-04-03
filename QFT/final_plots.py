import numpy as np
from scipy.optimize import curve_fit
import matplotlib as mpl
import matplotlib.pyplot as plt

maxqubit = 22   
xaxis = np.arange(1, maxqubit + 1, 1)

tntimes = list()

with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/HS/time_arrays/SV_times.csv") as fp:
    lines = fp.readlines()
    for l in lines:
        l.strip("\n")
        l = "[" + l + "]"
        tntimes.append(np.array(eval(l)))

tntot = tntimes[0]
tntot_err = tntimes[1]

def f(x, a, b , c):
    return a * np.exp(b * x) + c

def g(y, d, e):
    return d * y + e

popttntot, pcovtntot = curve_fit(g, xaxis, tntot)   #TN TOT

yerr = tntot_err
plt.errorbar(xaxis, tntot, yerr=yerr, fmt='bo', ecolor='blue', label=' SV total time')
plt.plot(xaxis, g(xaxis, *popttntot), 'g--', label='fit: a*exp(b*x)+c, a=%.2e, b=%.2e, ' % tuple(popttntot)) #c=%.2e
plt.xlabel('# of qubits')
plt.ylabel('time [s]')
plt.legend(loc= 'upper left')
plt.title('State vector HS - total execution time') #- parameters: ntimes = 10^2, nsample = 10^4'
plt.grid()
plt.show()
#plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/HS/plots/HS_TN_times.pdf")
