import numpy as np

from qibo.models import Circuit
from qibo.models import QFT
from qibo import gates

from benchmarks.circuits import qasm

class HiddenShift(qasm.HiddenShift):

    def to_qasm(self):
        raise NotImplementedError

    def oracle(self):
        for i in range(self.nqubits // 2):
            yield gates.CZ(2 * i, 2 * i + 1)

    def __iter__(self):
        for i in range(self.nqubits):
            yield gates.H(i)
        for i, ish in enumerate(self.shift):
            if ish:
                yield gates.X(i)
        for gate in self.oracle():
            yield gate
        for i, ish in enumerate(self.shift):
            if ish:
                yield gates.X(i)
        for i in range(self.nqubits):
            yield gates.H(i)
        for gate in self.oracle():
            yield gate
        for i in range(self.nqubits):
            yield gates.H(i)
        yield gates.M(*range(self.nqubits))