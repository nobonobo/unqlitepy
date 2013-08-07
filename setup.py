
import sys
import os
from setuptools import setup, Extension
import subprocess
from distutils.command.install import install

root = os.path.dirname(__file__)

class InstallWrap(install):
    def run(self):
        subprocess.check_call(['make', '-C', 'unqlitepy'])
        build_py.run(self)


setup (name = 'unqlitepy',
    version = '0.2.0',
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
    package_data = {
        '': ['Makefile'],
    },
    install_requires=['ctypesgen'],
    zip_safe=False,
)
