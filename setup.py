
import sys
import os
from setuptools import setup, Extension
import subprocess
from distutils.command.build_py import build_py

if sys.platform=='darwin':
    dylib = 'libunqlite.dylib'
else:
    dylib = 'libunqlite.so.1.0'

#root = os.path.dirname(__file__)

class BuildWrap(build_py):
    def build_modules(self):
        subprocess.check_call(['make'])
        build_py.build_modules(self)

setup (name = 'UnQLitePy',
    version = '0.1.0',
    description = 'UnQLite Binding for Python',
    author = 'Noboru Irieda',
    author_email = 'noboru@irieda.com',
    license = "BSD",
    url = 'https://github.com/nobonobo/unqlitepy',
    long_description = open('README.md').read(),
    cmdclass={"build_py": BuildWrap},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    py_modules = ['unqlite', 'unqlitepy'],
    include_package_data=True,
    data_files = [('', [dylib])],
    setup_requires=['ctypesgen'],
    zip_safe=False,
)
