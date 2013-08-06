unqlitepy
=============

UnQLite for Python Binding

## Install

```sh
> sudo pip install unqlitepy
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
from unqlitepy import UnQLite

with UnQLite(':mem:') as db:
    db.store('test', 'hello!')
    print db.fetch('test') # -> hello!
    db.append('test', ' world!')
    print db.fetch('test') # -> hello! world!

    db.delete('test')
    for i in range(25):
        db.store('test{0}'.format(i), 'hello!')
        db.store('etst{0}'.format(i), 'hello!')
        if i%5==0:
            db.delete('etst{0}'.format(i))

    @UnQLite.FetchCallback
    def f(output, outlen, udata):
        output = (c_char*outlen).from_address(output).raw
        print locals()
        return UNQLITE_OK

    db.fetch_cb('test0', f)

    sample = (
        "print 'hello!\n';"
        "db_create('users'); /* Create the collection users */"
        "db_create('hoges');"
        " /* Store something */ "
        "db_store('users',{ 'name' : 'dean' , 'age' : 32 });"
        "db_store('hoges',{ 'name' : 'dean' , 'age' : 32 });"
        "db_store('users',{ 'name' : 'chems' , 'age' : 27 });"
        "db_store('hoges',{ 'name' : 'chems' , 'age' : 27 });"
        "print db_fetch_all('users')..'\n';"
        "/*print db_reset_record_cursor('users')..'\n';*/"
        "while( ($rec = db_fetch('users')) != NULL ){"
        "  print $rec; print '\n';"
        "}"
    )

    with db.compile(sample) as vm:
        vm.execute()
        with vm.new_scalar() as sv, vm.new_array() as av:
            print sv, sv.is_scalar()
            print av, av.is_json_array()

    db.fetch_cb('users', f)

    with db.cursor() as cursor:
        cursor.first()
        cursor.seek('test20')
        while cursor.valid():
            print repr(cursor.key()), repr(cursor.value())
            cursor.next()
```
