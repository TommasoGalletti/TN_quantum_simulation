import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

import quimb as qu
import quimb.tensor as qtn

bigN = 40

totaltimevec = list()
processtimevec = list()
nvec = list()


for n in range(bigN):
    # Number of qubits
    nvec.append(n + 1)
    N = n + 1

    #registro ordine qubit
    regs = list(range(N))

    circ = qtn.Circuit(N)

    t0 = timeit.default_timer()     #tempo totale (default_timer() for device agnosticism)
    tprocess0 = time.process_time() #tempo CPU

    for i in range(N):
        circ.apply_gate('H', regs[i])                               #first we apply an Hadamard gate to the i-th qb

        for j in range(i + 1, N):
            theta = np.pi / 2 ** (j - i)                            #calculating theta angle, which we feed as a parameter to the CU1 gate
            circ.apply_gate('CU1', theta, regs[i], regs[j])         #we apply a controlled unitary (1) gate to gate i and all gates below i
            
    for i in range(N // 2):
        circ.apply_gate('SWAP', regs[i], regs[N - i - 1])           #swap gates

    for b in circ.sample(100000):                                        #sample results (1 time)
        print(b)

    #use: Counter(circ.sample(n)) to count resulting bit strings

    t1 = timeit.default_timer()     #final total time
    tprocess1 = time.process_time() #final CPU time

    totaltimevec.append(t1 - t0)    #save time in vector
    processtimevec.append(tprocess1 - tprocess0)    #""


fig1, ax1 = plt.subplots()          #total time
ax1.plot(nvec, totaltimevec, 'ro')
ax1.set_title('total time')
ax1.set_ylabel('time [s]')
ax1.set_xlabel('# of qubits')
ax1.grid()

plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/test_total_time_QFT.pdf")

fig2, ax2 = plt.subplots()          #CPU time
ax2.plot(nvec, processtimevec, 'ro')
ax2.set_title('CPU time')
ax2.set_ylabel('time [s]')
ax2.set_xlabel('# of qubits')
ax2.grid()

plt.savefig("c:/Users/tommy/OneDrive/Documenti/GitHub/test_process_time_QFT.pdf")

"""circ.psi.draw(color=['H', 'CU1', 'SWAP'])                       #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])                #circuit drawing - focus on qubit paths"""


#for b in range(2**N):
#print("x = 000, c = <x|U|psi0> = ", circ.amplitude('000'))           #compute c = <x|U|psi0> (x = 00, U circuit, psi0 initial state)