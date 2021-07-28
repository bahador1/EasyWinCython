from distutils.core import setup
from Cython.Build import cythonize

# setup(ext_modules = cythonize('tax_c.pyx'))
# setup(ext_modules = cythonize('tax_c_nogil.pyx'))
setup(ext_modules = cythonize('tax_c_c.pyx'))