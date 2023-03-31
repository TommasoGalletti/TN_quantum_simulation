import numpy as np
from scipy.optimize import curve_fit
import matplotlib as mpl
import matplotlib.pyplot as plt

maxqubit = 30

#CAMBIA NOME FILE TRA SV E TN
loaded_vecs = np.loadtxt('c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/time_arrays/TN_times.csv')

meantotaltime = loaded_vecs[0]
totaltimeerror = loaded_vecs[1]
meanprocesstime = loaded_vecs[2]
processtimeerror = loaded_vecs[3]

def f(x, a, b , c):
    return a * np.exp(b * x) + c

xaxis = np.arange(1, maxqubit + 1, 1)

popt, pcov = curve_fit(f, xaxis, meantotaltime)

#plt.plot(xaxis, meantotaltime, 'bo', label='total time data')
yerr = totaltimeerror
plt.errorbar(xaxis, meantotaltime, yerr=yerr)
plt.plot(xaxis, f(xaxis, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.xlabel('# of qubits')
plt.ylabel('total time [s]')
plt.legend()
plt.show()


#total time
fig2, ax2 = plt.figure()
y = meantotaltime
yerr = totaltimeerror
ax2.set_ylim(bottom= 0) #???
plt.errorbar(xaxis, y, yerr=yerr)
fig2.suptitle('Total time')
fig2.supxlabel('# of qubits')
fig2.supylabel('time [s]')
#plt.legend(loc='upper left')
#plt.savefig("~/QFT/QFT_SV_total_time_error.pdf")
plt.show()

#CPU time
fig4, ax4 = plt.figure()
y = meanprocesstime
yerr = processtimeerror
ax4.set_ylim(bottom= 0) #???
plt.errorbar(xaxis, y, yerr=yerr)
fig4.suptitle('CPU time')
fig4.supxlabel('# of qubits')
fig4.supylabel('time [s]')
#plt.legend(loc='upper left')
#plt.savefig("~/QFT/QFT_SV_CPU_time_error.pdf")
plt.show()
