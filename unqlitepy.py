#!/usr/bin/env python
# encoding: utf-8

import sys
import os

if sys.platform=='linux2':
    libs = os.environ.get('LD_LIBRARY_PATH','').split(':')
    libs.append(os.path.dirname(__file__))
    os.environ['LD_LIBRARY_PATH'] = ':'.join(libs)

from unqlite import *

OutputCallback = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None))

class Value(object):
    is_types = ['int', 'float', 'bool', 'string', 'null', 'numeric',
        'callable', 'scalar', 'json_array', 'json_object', 'resource', 'empty']
    to_types = ['int', 'bool', 'int64', 'double', 'string', 'resource']
    def __init__(self, vm, ptr):
        self.vm = vm
        self.ptr = ptr
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False
    def close(self):
        if self.ptr:
            unqlite_vm_release_value(self.vm, self.ptr)
            self.ptr = None
    for tp in is_types:
        exec("""def is_{0}(self):
            return bool(unqlite_value_is_{0}(self.ptr))""".format(tp))
    for tp in to_types:
        exec("""def to_{0}(self):
            return unqlite_value_to_{0}(self.ptr)""".format(tp))
    def set(self, val):
        if isinstance(val, int):
            res = unqlite_value_int(self.ptr, val)
        elif isinstance(val, long):
            res = unqlite_value_int64(self.ptr, unqlite_int64(val))
        elif isinstance(val, bool):
            res = unqlite_value_bool(self.ptr, int(val))
        elif val is None:
            res = unqlite_value_null(self.ptr)
        elif isinstance(val, float):
            res = unqlite_value_double(self.ptr, val)
        elif isinstance(val, str):
            res = unqlite_value_string(self.ptr, val, len(val))
        elif isinstance(val, unocode):
            val = val.encode('utf-8')
            res = unqlite_value_string(self.ptr, val, len(val))
        elif isinstance(val, POINTER):
            res = unqlite_value_resource(self.ptr, val)
        else:
            assert 0, "Unknown Type: {0}".format(repr(val))
        assert UNQLITE_OK == res, res

class VM(object):

    def __init__(self, db, code):
        self.vm = POINTER(unqlite_vm)()
        res = unqlite_compile(db, code, -1, byref(self.vm))
        assert UNQLITE_OK == res, res
        self._config(UNQLITE_VM_CONFIG_OUTPUT, self.outputcb)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def close(self):
        if self.vm:
            unqlite_vm_release(self.vm)
            self.vm = None

    def reset(self):
        res = unqlite_vm_reset(self.db)
        assert UNQLITE_OK == res, res

    @OutputCallback
    def outputcb(output, outlen, udata):
        output = (c_char*outlen).from_address(output).raw
        sys.stdout.write(output)
        return UNQLITE_OK

    def _config(self, verb, *args):
        res = unqlite_vm_config(self.vm, verb, *args)
        assert UNQLITE_OK == res, res

    def execute(self):
        res = unqlite_vm_exec(self.vm)
        assert UNQLITE_OK == res, res

    def new_scalar(self):
        return Value(self.vm, unqlite_vm_new_scalar(self.vm))

    def new_array(self):
        return Value(self.vm, unqlite_vm_new_array(self.vm))

    def extract(self, name):
        return Value(self.vm, unqlite_vm_extract_variable(self.vm, name))

    def dump(self, callback, udata):
        res = unqlite_vm_dump(self.vm, callback, udata)
        assert UNQLITE_OK == res, res


class VMfromFile(VM):
    def __init__(self, db, fpath):
        self.vm = POINTER(unqlite_vm)()
        res = unqlite_compile_file(db, fpath, byref(self.vm))
        assert UNQLITE_OK == res, res
        self._config(UNQLITE_VM_CONFIG_OUTPUT, self.outputcb)


class Cursor(object):
    
    def __init__(self, db):
        self.db = db
        self.cursor = POINTER(unqlite_kv_cursor)()
        res = unqlite_kv_cursor_init(db, byref(self.cursor))
        assert UNQLITE_OK == res, res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def close(self):
        if self.cursor:
            unqlite_kv_cursor_release(self.db, self.cursor)
            self.cursor = None
    
    def seek(self, key, flags=UNQLITE_CURSOR_MATCH_EXACT):
        res = unqlite_kv_cursor_seek(self.cursor, key, len(key), flags)
        assert UNQLITE_OK == res, res

    def first(self):
        return unqlite_kv_cursor_first_entry(self.cursor)

    def last(self):
        return unqlite_kv_cursor_last_entry(self.cursor)

    def valid(self):
        return bool(unqlite_kv_cursor_valid_entry(self.cursor))

    def next(self):
        return unqlite_kv_cursor_next_entry(self.cursor)

    def prev(self):
        return unqlite_kv_cursor_prev_entry(self.cursor)

    def reset(self):
        return unqlite_kv_cursor_reset(self.cursor)

    def delete(self):
        return unqlite_kv_cursor_delete_entry(self.cursor)
    
    def key(self, max=65536):
        buff = create_string_buffer(max)
        length = unqlite_int64(max)
        res = unqlite_kv_cursor_key(self.cursor, byref(buff), byref(length))
        assert UNQLITE_OK == res, res
        return buff.raw[:length.value]

    def key_cb(self, callback, udata=None):
        res = unqlite_kv_cursor_key_callback(self.cursor, callback, udata)
        assert UNQLITE_OK == res, res

    def value(self, max=65536):
        buff = create_string_buffer(max)
        length = unqlite_int64(max)
        res = unqlite_kv_cursor_data(self.cursor, byref(buff), byref(length))
        assert UNQLITE_OK == res, res
        return buff.raw[:length.value]

    def value_cb(self, callback, udata=None):
        res = unqlite_kv_cursor_value_callback(self.cursor, callback, udata)
        assert UNQLITE_OK == res, res

class UnQLite(object):

    def __init__(self, uri, flags=UNQLITE_OPEN_CREATE):
        self.db = POINTER(unqlite)()
        unqlite_open(byref(self.db), uri, UNQLITE_OPEN_CREATE)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def close(self):
        if self.db:
            unqlite_close(self.db)
            self.db = None

    def _config(self, verb, param, udata=None):
        res = unqlite_kv_config(self.vm, verb, param)
        assert UNQLITE_OK == res, res

    def store(self, key, value):
        res = unqlite_kv_store(self.db, key, len(key), value, len(value))
        assert UNQLITE_OK == res, res

    def append(self, key, value):
        res = unqlite_kv_append(self.db, key, len(key), value, len(value))
        assert UNQLITE_OK == res, res

    def exists(self, key):
        length = unqlite_int64(0)
        res = unqlite_kv_fetch(self.db, key, len(key), None, byref(length))
        return UNQLITE_OK == res

    def fetch(self, key, max=65536):
        buff = create_string_buffer(max)
        length = unqlite_int64(max)
        res = unqlite_kv_fetch(self.db, key, len(key), byref(buff), byref(length))
        assert UNQLITE_OK == res, res
        return buff.raw[:length.value]

    def fetch_cb(self, key, callback, udata=None):
        res = unqlite_kv_fetch_callback(self.db, key, len(key), callback, udata)
        assert UNQLITE_OK == res, res

    def delete(self, key):
        res = unqlite_kv_delete(self.db, key, len(key))
        assert UNQLITE_OK == res, res

    def begin(self):
        res = unqlite_begin(self.db)
        assert UNQLITE_OK == res, res

    def commit(self):
        res = unqlite_commit(self.db)
        assert UNQLITE_OK == res, res

    def rollback(self):
        res = unqlite_rollback(self.db)
        assert UNQLITE_OK == res, res

    def compile(self, code):
        return VM(self.db, code)

    def compile_file(self, fpath):
        return VMfromFile(self.db, fpath)

    def cursor(self):
        return Cursor(self.db)

    def mmap(self, fname):
        return MMap(self.db, fname)

    def random_num(self):
        return unqlite_util_random_num(self.db)

    def random_string(self, length):
        buff = create_string_buffer(length+3)
        res = unqlite_util_random_string(self.db, byref(buff), length)
        assert UNQLITE_OK == res, res
        return buff.raw[:length]

class MMap(object):
    def __init__(self, db, fname):
        self.db = db
        self.ptr = c_void_p()
        self.size = unqlite_int64(os.stat(fname).st_size)
        res = unqlite_util_load_mmaped_file(fname, byref(self.ptr), byref(self.size))
        assert UNQLITE_OK == res, res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False

    def __len__(self):
        return self.size

    def close(self):
        if self.ptr:
            unqlite_util_release_mmaped_file(self.ptr, self.size)
            self.ptr = None

    def store(self, key):
        res = unqlite_kv_store(self.db, key, len(key), self.ptr, self.size)
        assert UNQLITE_OK == res, res

def lib_config(self, verb, *args):
    res = unqlite_lib_config(self.vm, verb, *args)
    assert UNQLITE_OK == res, res

def config(self, verb, *args):
    res = unqlite_config(self.vm, verb, *args)
    assert UNQLITE_OK == res, res

if __name__=='__main__':

    with UnQLite(':mem:') as db:
        db.store('test', 'hello!')
        print db.fetch('test')
        db.append('test', ' world!')
        print db.fetch('test')

        db.delete('test')
        for i in range(25):
            db.store('test{0}'.format(i), 'hello!')
            db.store('etst{0}'.format(i), 'hello!')
            if i%5==0:
                db.delete('etst{0}'.format(i))

        @OutputCallback
        def f(output, outlen, udata):
            output = (c_char*outlen).from_address(output).raw
            print locals()
            return UNQLITE_OK

        db.fetch_cb('test0', f)
        print 'test0', db.exists('test0')
        print 'test100', db.exists('test100')

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

        with db.mmap('Makefile') as mm:
            mm.store('makefile')

        db.fetch_cb('makefile', f)
