
import sys
import os
from setuptools import setup, Extension
import subprocess
from setuptools.command.install import install

root = os.path.dirname(__file__)

if sys.platform=='darwin':
    dllname = 'libunqlite.dylib'
else:
    dllname = 'libunqlite.so.1.0'

class InstallWrap(install):
    def run(self):
        install.run(self)
        subprocess.check_call(['make', '-C', 'unqlitepy'],
            cwd=self.install_lib)


setup (name = 'unqlitepy',
    version = '0.3.0',
    description = 'UnQLite Binding for Python',
    author = 'Noboru Irieda',
    author_email = 'noboru@irieda.com',
    license = "BSD",
    keywords=['database', 'kvs', 'unqlite'],
    url = 'https://github.com/nobonobo/unqlitepy',
    #long_description = open('README.md').read(),
    cmdclass={"install": InstallWrap},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",

    ],
    packages = ['unqlitepy'],
    include_package_data=True,
    #package_data = {
    #    '': ['Makefile', dllname],
    #},
    install_requires=['ctypesgen'],
    setup_requires=['ctypesgen'],
    requires=['ctypesgen'],
    zip_safe=False,
)
