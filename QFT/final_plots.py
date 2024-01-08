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

"""
def g(y, d, e):
    return d * y + e
"""
popttntot, pcovtntot = curve_fit(f, xaxis, tntot)   #TN TOT

#print(tuple(popttntot))

yerr = tntot_err
plt.errorbar(xaxis, tntot, yerr=yerr, fmt='go', ecolor='blue', label=' SV total time')
plt.plot(xaxis, f(xaxis, *popttntot), 'g--', label='fit: a*exp(b*x)+c, a=%.2e, b=%.2e, c=%.2e' % tuple(popttntot)) #c=%.2e
plt.xlabel('# of qubits')
plt.ylabel('time [s]')
plt.yscale('log')
plt.legend(loc= 'upper left')
plt.title('TN QFT - total execution time') #- parameters: ntimes = 10^2, nsample = 10^4'
plt.grid()
plt.show()
#plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/plots/QFT_TN_times_log.pdf")
