unqlitepy
=============

UnQLite for Python Binding

## Build

> python setup.py bdist_egg


## Install

> sudo python setup.py install

or 

> sudo easy_install dist/UnQLitePy-0.1.0-py2.7.egg

or 

> virtualenv sample
> cd sample
> bin/easy_install UnQLitePy-0.1.0-py2.7.egg
...
Finished processing dependencies for UnQLitePy==0.1.0

## Usage

> from unqlitepy import UnQLite
> db = UnQLite(':mem:')
> db.store('hoge', 'value')
> db.fetch('hoge')
'value'
