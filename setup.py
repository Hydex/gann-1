from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Population Class',
  ext_modules = cythonize("MLP.py"),
)

#python setup.py build_ext --inplace
