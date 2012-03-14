from psg.util.misc import pfb2pfa as pfb2pfa_orig
from pfb2pfa import pfb2pfa as pfb2pfa_cython
from io import StringIO
import timeit


iterations = 10

pfb = open('../examples/regular.pfb', 'rb')


def b2a_orig():
    pfb.seek(0)
    pfa = StringIO()
    pfb2pfa_orig(pfb, pfa)
    pfa.close()


def b2a_cython():
    pfb.seek(0)
    pfa = StringIO()
    pfb2pfa_cython(pfb, pfa)
    pfa.close()


time = timeit.timeit(b2a_orig, number=iterations)
print('python: {} seconds'.format(time))

time = timeit.timeit(b2a_cython, number=iterations)
print('cython: {} seconds'.format(time))


pfb.close()

