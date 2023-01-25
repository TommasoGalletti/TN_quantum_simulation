#config InlineBackend.figure_formats = ['svg']
import quimb as qu
import quimb.tensor as qtn

data = qu.bell_state('psi-').reshape(2, 2)
inds = ('k0', 'k1')
tags = ('KET',)

ket = qtn.Tensor(data=data, inds=inds, tags=tags)
print(ket)
#Tensor(shape=(2, 2), inds=('k0', 'k1'), tags=oset(['KET']))

ket.draw()
