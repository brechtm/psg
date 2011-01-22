#from psg.util.misc import pfb2pfa   # plain python
from pfb2pfa import pfb2pfa         # cython
import timeit

pfb = open('../examples/regular.pfb', 'rb')
pfa = open('regular.pfa', 'w')

def b2a():
    pfb2pfa(pfb, pfa)

time = timeit.timeit(b2a, number=1)

print('{} seconds'.format(time))

pfa.close()
pfb.close()
