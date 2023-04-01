import numpy as np
from scipy.optimize import curve_fit
import matplotlib as mpl
import matplotlib.pyplot as plt

maxqubit = 28
xaxis = np.arange(1, maxqubit + 1, 1)

tntot = list()
tntot_err = list()
tncpu = list()
tncpu_err = list()

with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/time_arrays/TN_times.csv") as fp:
    lines = fp.readlines()

    tntot = [eval(x) for x in lines[0]]
    tntot_err = list(map(float, lines[1]))
    tncpu = list(map(float, lines[2]))
    tncpu_err = list(map(float, lines[3]))  

svtot = list()
svtot_err = list()
svcpu = list()
svcpu_err = list()

with open("c:/Users/tommy/OneDrive/Documenti/GitHub/TN_quantum_simulation/QFT/time_arrays/TN_times.csv") as fp:
    lines = fp.readlines()

    svtot = lines[0]
    svtot_err = lines[1]
    svcpu = lines[2]
    svcpu_err = lines[3]

def f(x, a, b , c):
    return a * np.exp(b * x) + c

popttntot, pcovtntot = curve_fit(f, xaxis, tntot)   #TN TOT
popttncpu, pcovtncpu = curve_fit(f, xaxis, tncpu)   #TN CPU
poptsvtot, pcovsvtot = curve_fit(f, xaxis, svtot)   #SV TOT
poptsvcpu, pcovsvcpu = curve_fit(f, xaxis, svcpu)   #SV CPU


yerr = tntot_err
plt.errorbar(xaxis, tntot, yerr=yerr, lolims= 0, label=' TN total time')
plt.plot(xaxis, f(xaxis, *popttntot), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popttntot))
plt.xlabel('# of qubits')
plt.ylabel('TN total time [s]')
plt.legend()
plt.show()
#plt.savefig("~/QFT/QFT_TN_tot.pdf")

yerr = tncpu_err
plt.errorbar(xaxis, tncpu, yerr=yerr, lolims= 0, label=' TN CPU time')
plt.plot(xaxis, f(xaxis, *popttncpu), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popttncpu))
plt.xlabel('# of qubits')
plt.ylabel('TN CPU time [s]')
plt.legend()
plt.show()
#plt.savefig("~/QFT/QFT_TN_cpu.pdf")

yerr = svtot_err
plt.errorbar(xaxis, svtot, yerr=yerr, lolims= 0, label=' TN CPU time')
plt.plot(xaxis, f(xaxis, *poptsvtot), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(poptsvtot))
plt.xlabel('# of qubits')
plt.ylabel('SV tot time [s]')
plt.legend()
plt.show()
#plt.savefig("~/QFT/QFT_SV_tot.pdf")

yerr = svcpu_err
plt.errorbar(xaxis, svcpu, yerr=yerr, lolims= 0, label=' TN CPU time')
plt.plot(xaxis, f(xaxis, *poptsvcpu), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(poptsvcpu))
plt.xlabel('# of qubits')
plt.ylabel('SV CPU time [s]')
plt.legend()
plt.show()
#plt.savefig("~/QFT/QFT_SV_cpu.pdf")

"""
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
"""
