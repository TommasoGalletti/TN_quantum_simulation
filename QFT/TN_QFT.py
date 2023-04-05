import numpy as np
import time
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import quimb as qu
import quimb.tensor as qtn

N = 80

def build_QFT(N, regs):
    for h in range(N):
        circ.apply_gate('H', regs[h])                               
        for j in range(h + 1, N):
            theta = np.pi / 2 ** (j - h)    #rotation angle   
            circ.apply_gate('CU1', theta, regs[h], regs[j])
                
    for s in range(N // 2):
        circ.apply_gate('SWAP', regs[s], regs[N - s - 1])

regs = list(range(N))
circ = qtn.Circuit(N)

build_QFT(N, regs)

circ.psi.draw(color=['H', 'CU1', 'SWAP'])                   #circuit drawing - focus on gate types
circ.psi.draw(color=[f'I{i}' for i in range(N)])            #circuit drawing - focus on qubit paths



circ.psi.draw(
    custom_colors=[(0.8, 0.3, 0.7)] + [(0.3, 0.8, 0.2)] * 4,
    edge_color='black',
    edge_alpha=1.0,
    edge_scale=1.0,
    arrow_overhang=1.0,
    arrow_linewidth=4,
    node_size=400,
    node_outline_darkness=0.0,
    node_outline_size=2.5,
    legend=False,
)