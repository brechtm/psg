from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pfb2pfa", ["pfb2pfa.pyx"])]

setup(
  name = 'PSG pfb2pfa',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)