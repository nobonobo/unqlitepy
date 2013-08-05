unqlitepy
=============

UnQLite for Python Binding

## Prerequire

```sh
> sudo pip install ctypesgen
```

## Install

```sh
> sudo pip install git+https://github.com/nobonobo/unqlitepy.git
...
Successfully installed UnQLitePy
Cleaning up...
```
or 

```sh
> virtualenv sample
> cd sample
> bin/pip install git+https://github.com/nobonobo/unqlitepy.git
...
Successfully installed UnQLitePy
Cleaning up...
```

## Usage

```python
> from unqlitepy import UnQLite
> db = UnQLite(':mem:')
> db.store('hoge', 'value')
> db.fetch('hoge')
'value'
```
