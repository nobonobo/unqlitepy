'''Wrapper for unqlite.h

Generated with:
/Users/nobo/bin/ctypesgen.py unqlite.h -L ./ -l unqlite -o unqlite.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = ['./']

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs(['./'])

# Begin libraries

_libs["unqlite"] = load_library("unqlite")

# 1 libraries
# End libraries

# No modules

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 563
class struct_unqlite_io_methods(Structure):
    pass

unqlite_io_methods = struct_unqlite_io_methods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 91

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 743
class struct_unqlite_kv_methods(Structure):
    pass

unqlite_kv_methods = struct_unqlite_kv_methods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 92

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 730
class struct_unqlite_kv_engine(Structure):
    pass

unqlite_kv_engine = struct_unqlite_kv_engine # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 93

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 94
class struct_jx9_io_stream(Structure):
    pass

unqlite_io_stream = struct_jx9_io_stream # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 94

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 95
class struct_jx9_context(Structure):
    pass

unqlite_context = struct_jx9_context # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 95

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 96
class struct_jx9_value(Structure):
    pass

unqlite_value = struct_jx9_value # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 96

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 609
class struct_unqlite_vfs(Structure):
    pass

unqlite_vfs = struct_unqlite_vfs # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 97

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 98
class struct_unqlite_vm(Structure):
    pass

unqlite_vm = struct_unqlite_vm # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 98

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 99
class struct_unqlite(Structure):
    pass

unqlite = struct_unqlite # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 99

sxi64 = c_longlong # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 191

sxu64 = c_ulonglong # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 192

ProcConsumer = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)) # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 195

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 277
class struct_SyMutexMethods(Structure):
    pass

SyMutexMethods = struct_SyMutexMethods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 197

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 264
class struct_SyMemMethods(Structure):
    pass

SyMemMethods = struct_SyMemMethods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 198

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 215
class struct_SyString(Structure):
    pass

SyString = struct_SyString # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 199

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 204
class struct_syiovec(Structure):
    pass

syiovec = struct_syiovec # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 200

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 201
class struct_SyMutex(Structure):
    pass

SyMutex = struct_SyMutex # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 201

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 221
class struct_Sytm(Structure):
    pass

Sytm = struct_Sytm # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 202

struct_syiovec.__slots__ = [
    'pBase',
    'nLen',
]
struct_syiovec._fields_ = [
    ('pBase', POINTER(None)),
    ('nLen', c_ulong),
]

struct_SyString.__slots__ = [
    'zString',
    'nByte',
]
struct_SyString._fields_ = [
    ('zString', String),
    ('nByte', c_uint),
]

struct_Sytm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_zone',
    'tm_gmtoff',
]
struct_Sytm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_zone', String),
    ('tm_gmtoff', c_long),
]

struct_SyMemMethods.__slots__ = [
    'xAlloc',
    'xRealloc',
    'xFree',
    'xChunkSize',
    'xInit',
    'xRelease',
    'pUserData',
]
struct_SyMemMethods._fields_ = [
    ('xAlloc', CFUNCTYPE(UNCHECKED(POINTER(None)), c_uint)),
    ('xRealloc', CFUNCTYPE(UNCHECKED(POINTER(None)), POINTER(None), c_uint)),
    ('xFree', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('xChunkSize', CFUNCTYPE(UNCHECKED(c_uint), POINTER(None))),
    ('xInit', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('xRelease', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('pUserData', POINTER(None)),
]

ProcMemError = CFUNCTYPE(UNCHECKED(c_int), POINTER(None)) # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 275

struct_SyMutexMethods.__slots__ = [
    'xGlobalInit',
    'xGlobalRelease',
    'xNew',
    'xRelease',
    'xEnter',
    'xTryEnter',
    'xLeave',
]
struct_SyMutexMethods._fields_ = [
    ('xGlobalInit', CFUNCTYPE(UNCHECKED(c_int), )),
    ('xGlobalRelease', CFUNCTYPE(UNCHECKED(None), )),
    ('xNew', CFUNCTYPE(UNCHECKED(POINTER(SyMutex)), c_int)),
    ('xRelease', CFUNCTYPE(UNCHECKED(None), POINTER(SyMutex))),
    ('xEnter', CFUNCTYPE(UNCHECKED(None), POINTER(SyMutex))),
    ('xTryEnter', CFUNCTYPE(UNCHECKED(c_int), POINTER(SyMutex))),
    ('xLeave', CFUNCTYPE(UNCHECKED(None), POINTER(SyMutex))),
]

unqlite_real = c_double # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 342

unqlite_int64 = sxi64 # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 344

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 520
class struct_unqlite_file(Structure):
    pass

unqlite_file = struct_unqlite_file # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 519

struct_unqlite_file.__slots__ = [
    'pMethods',
]
struct_unqlite_file._fields_ = [
    ('pMethods', POINTER(unqlite_io_methods)),
]

struct_unqlite_io_methods.__slots__ = [
    'iVersion',
    'xClose',
    'xRead',
    'xWrite',
    'xTruncate',
    'xSync',
    'xFileSize',
    'xLock',
    'xUnlock',
    'xCheckReservedLock',
    'xSectorSize',
]
struct_unqlite_io_methods._fields_ = [
    ('iVersion', c_int),
    ('xClose', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file))),
    ('xRead', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), POINTER(None), unqlite_int64, unqlite_int64)),
    ('xWrite', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), POINTER(None), unqlite_int64, unqlite_int64)),
    ('xTruncate', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), unqlite_int64)),
    ('xSync', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), c_int)),
    ('xFileSize', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), POINTER(unqlite_int64))),
    ('xLock', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), c_int)),
    ('xUnlock', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), c_int)),
    ('xCheckReservedLock', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file), POINTER(c_int))),
    ('xSectorSize', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_file))),
]

struct_unqlite_vfs.__slots__ = [
    'zName',
    'iVersion',
    'szOsFile',
    'mxPathname',
    'xOpen',
    'xDelete',
    'xAccess',
    'xFullPathname',
    'xTmpDir',
    'xSleep',
    'xCurrentTime',
    'xGetLastError',
]
struct_unqlite_vfs._fields_ = [
    ('zName', String),
    ('iVersion', c_int),
    ('szOsFile', c_int),
    ('mxPathname', c_int),
    ('xOpen', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), String, POINTER(unqlite_file), c_uint)),
    ('xDelete', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), String, c_int)),
    ('xAccess', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), String, c_int, POINTER(c_int))),
    ('xFullPathname', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), String, c_int, String)),
    ('xTmpDir', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), String, c_int)),
    ('xSleep', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), c_int)),
    ('xCurrentTime', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), POINTER(Sytm))),
    ('xGetLastError', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_vfs), c_int, String)),
]

pgno = sxu64 # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 651

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 657
class struct_unqlite_page(Structure):
    pass

unqlite_page = struct_unqlite_page # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 656

struct_unqlite_page.__slots__ = [
    'zData',
    'pUserData',
]
struct_unqlite_page._fields_ = [
    ('zData', POINTER(c_ubyte)),
    ('pUserData', POINTER(None)),
]

unqlite_kv_handle = POINTER(None) # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 666

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 674
class struct_unqlite_kv_io(Structure):
    pass

unqlite_kv_io = struct_unqlite_kv_io # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 673

struct_unqlite_kv_io.__slots__ = [
    'pHandle',
    'pMethods',
    'xGet',
    'xLookup',
    'xNew',
    'xWrite',
    'xDontWrite',
    'xDontJournal',
    'xDontMkHot',
    'xPageRef',
    'xPageUnref',
    'xPageSize',
    'xReadOnly',
    'xTmpPage',
    'xSetUnpin',
    'xSetReload',
    'xErr',
]
struct_unqlite_kv_io._fields_ = [
    ('pHandle', unqlite_kv_handle),
    ('pMethods', POINTER(unqlite_kv_methods)),
    ('xGet', CFUNCTYPE(UNCHECKED(c_int), unqlite_kv_handle, pgno, POINTER(POINTER(unqlite_page)))),
    ('xLookup', CFUNCTYPE(UNCHECKED(c_int), unqlite_kv_handle, pgno, POINTER(POINTER(unqlite_page)))),
    ('xNew', CFUNCTYPE(UNCHECKED(c_int), unqlite_kv_handle, POINTER(POINTER(unqlite_page)))),
    ('xWrite', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xDontWrite', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xDontJournal', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xDontMkHot', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xPageRef', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xPageUnref', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_page))),
    ('xPageSize', CFUNCTYPE(UNCHECKED(c_int), unqlite_kv_handle)),
    ('xReadOnly', CFUNCTYPE(UNCHECKED(c_int), unqlite_kv_handle)),
    ('xTmpPage', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), unqlite_kv_handle)),
    ('xSetUnpin', CFUNCTYPE(UNCHECKED(None), unqlite_kv_handle, CFUNCTYPE(UNCHECKED(None), POINTER(None)))),
    ('xSetReload', CFUNCTYPE(UNCHECKED(None), unqlite_kv_handle, CFUNCTYPE(UNCHECKED(None), POINTER(None)))),
    ('xErr', CFUNCTYPE(UNCHECKED(None), unqlite_kv_handle, String)),
]

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 704
class struct_unqlite_kv_cursor(Structure):
    pass

unqlite_kv_cursor = struct_unqlite_kv_cursor # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 703

struct_unqlite_kv_cursor.__slots__ = [
    'pStore',
]
struct_unqlite_kv_cursor._fields_ = [
    ('pStore', POINTER(unqlite_kv_engine)),
]

struct_unqlite_kv_engine.__slots__ = [
    'pIo',
]
struct_unqlite_kv_engine._fields_ = [
    ('pIo', POINTER(unqlite_kv_io)),
]

struct_unqlite_kv_methods.__slots__ = [
    'zName',
    'szKv',
    'szCursor',
    'iVersion',
    'xInit',
    'xRelease',
    'xConfig',
    'xOpen',
    'xReplace',
    'xAppend',
    'xCursorInit',
    'xSeek',
    'xFirst',
    'xLast',
    'xValid',
    'xNext',
    'xPrev',
    'xDelete',
    'xKeyLength',
    'xKey',
    'xDataLength',
    'xData',
    'xReset',
    'xCursorRelease',
]
struct_unqlite_kv_methods._fields_ = [
    ('zName', String),
    ('szKv', c_int),
    ('szCursor', c_int),
    ('iVersion', c_int),
    ('xInit', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_engine), c_int)),
    ('xRelease', CFUNCTYPE(UNCHECKED(None), POINTER(unqlite_kv_engine))),
    ('xConfig', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_engine), c_int, c_void_p)),
    ('xOpen', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_engine), pgno)),
    ('xReplace', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_engine), POINTER(None), c_int, POINTER(None), unqlite_int64)),
    ('xAppend', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_engine), POINTER(None), c_int, POINTER(None), unqlite_int64)),
    ('xCursorInit', CFUNCTYPE(UNCHECKED(None), POINTER(unqlite_kv_cursor))),
    ('xSeek', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor), POINTER(None), c_int, c_int)),
    ('xFirst', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xLast', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xValid', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xNext', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xPrev', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xDelete', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor))),
    ('xKeyLength', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor), POINTER(c_int))),
    ('xKey', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None))),
    ('xDataLength', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor), POINTER(unqlite_int64))),
    ('xData', CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_kv_cursor), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None))),
    ('xReset', CFUNCTYPE(UNCHECKED(None), POINTER(unqlite_kv_cursor))),
    ('xCursorRelease', CFUNCTYPE(UNCHECKED(None), POINTER(unqlite_kv_cursor))),
]

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 802
if hasattr(_libs['unqlite'], 'unqlite_open'):
    unqlite_open = _libs['unqlite'].unqlite_open
    unqlite_open.argtypes = [POINTER(POINTER(unqlite)), String, c_uint]
    unqlite_open.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 803
if hasattr(_libs['unqlite'], 'unqlite_config'):
    _func = _libs['unqlite'].unqlite_config
    _restype = c_int
    _argtypes = [POINTER(unqlite), c_int]
    unqlite_config = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 804
if hasattr(_libs['unqlite'], 'unqlite_close'):
    unqlite_close = _libs['unqlite'].unqlite_close
    unqlite_close.argtypes = [POINTER(unqlite)]
    unqlite_close.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 807
if hasattr(_libs['unqlite'], 'unqlite_kv_store'):
    unqlite_kv_store = _libs['unqlite'].unqlite_kv_store
    unqlite_kv_store.argtypes = [POINTER(unqlite), POINTER(None), c_int, POINTER(None), unqlite_int64]
    unqlite_kv_store.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 808
if hasattr(_libs['unqlite'], 'unqlite_kv_append'):
    unqlite_kv_append = _libs['unqlite'].unqlite_kv_append
    unqlite_kv_append.argtypes = [POINTER(unqlite), POINTER(None), c_int, POINTER(None), unqlite_int64]
    unqlite_kv_append.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 809
if hasattr(_libs['unqlite'], 'unqlite_kv_store_fmt'):
    _func = _libs['unqlite'].unqlite_kv_store_fmt
    _restype = c_int
    _argtypes = [POINTER(unqlite), POINTER(None), c_int, String]
    unqlite_kv_store_fmt = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 810
if hasattr(_libs['unqlite'], 'unqlite_kv_append_fmt'):
    _func = _libs['unqlite'].unqlite_kv_append_fmt
    _restype = c_int
    _argtypes = [POINTER(unqlite), POINTER(None), c_int, String]
    unqlite_kv_append_fmt = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 811
if hasattr(_libs['unqlite'], 'unqlite_kv_fetch'):
    unqlite_kv_fetch = _libs['unqlite'].unqlite_kv_fetch
    unqlite_kv_fetch.argtypes = [POINTER(unqlite), POINTER(None), c_int, POINTER(None), POINTER(unqlite_int64)]
    unqlite_kv_fetch.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 812
if hasattr(_libs['unqlite'], 'unqlite_kv_fetch_callback'):
    unqlite_kv_fetch_callback = _libs['unqlite'].unqlite_kv_fetch_callback
    unqlite_kv_fetch_callback.argtypes = [POINTER(unqlite), POINTER(None), c_int, CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None)]
    unqlite_kv_fetch_callback.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 814
if hasattr(_libs['unqlite'], 'unqlite_kv_delete'):
    unqlite_kv_delete = _libs['unqlite'].unqlite_kv_delete
    unqlite_kv_delete.argtypes = [POINTER(unqlite), POINTER(None), c_int]
    unqlite_kv_delete.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 815
if hasattr(_libs['unqlite'], 'unqlite_kv_config'):
    _func = _libs['unqlite'].unqlite_kv_config
    _restype = c_int
    _argtypes = [POINTER(unqlite), c_int]
    unqlite_kv_config = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 818
if hasattr(_libs['unqlite'], 'unqlite_compile'):
    unqlite_compile = _libs['unqlite'].unqlite_compile
    unqlite_compile.argtypes = [POINTER(unqlite), String, c_int, POINTER(POINTER(unqlite_vm))]
    unqlite_compile.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 819
if hasattr(_libs['unqlite'], 'unqlite_compile_file'):
    unqlite_compile_file = _libs['unqlite'].unqlite_compile_file
    unqlite_compile_file.argtypes = [POINTER(unqlite), String, POINTER(POINTER(unqlite_vm))]
    unqlite_compile_file.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 820
if hasattr(_libs['unqlite'], 'unqlite_vm_config'):
    _func = _libs['unqlite'].unqlite_vm_config
    _restype = c_int
    _argtypes = [POINTER(unqlite_vm), c_int]
    unqlite_vm_config = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 821
if hasattr(_libs['unqlite'], 'unqlite_vm_exec'):
    unqlite_vm_exec = _libs['unqlite'].unqlite_vm_exec
    unqlite_vm_exec.argtypes = [POINTER(unqlite_vm)]
    unqlite_vm_exec.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 822
if hasattr(_libs['unqlite'], 'unqlite_vm_reset'):
    unqlite_vm_reset = _libs['unqlite'].unqlite_vm_reset
    unqlite_vm_reset.argtypes = [POINTER(unqlite_vm)]
    unqlite_vm_reset.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 823
if hasattr(_libs['unqlite'], 'unqlite_vm_release'):
    unqlite_vm_release = _libs['unqlite'].unqlite_vm_release
    unqlite_vm_release.argtypes = [POINTER(unqlite_vm)]
    unqlite_vm_release.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 824
if hasattr(_libs['unqlite'], 'unqlite_vm_dump'):
    unqlite_vm_dump = _libs['unqlite'].unqlite_vm_dump
    unqlite_vm_dump.argtypes = [POINTER(unqlite_vm), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None)]
    unqlite_vm_dump.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 825
if hasattr(_libs['unqlite'], 'unqlite_vm_extract_variable'):
    unqlite_vm_extract_variable = _libs['unqlite'].unqlite_vm_extract_variable
    unqlite_vm_extract_variable.argtypes = [POINTER(unqlite_vm), String]
    unqlite_vm_extract_variable.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 828
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_init'):
    unqlite_kv_cursor_init = _libs['unqlite'].unqlite_kv_cursor_init
    unqlite_kv_cursor_init.argtypes = [POINTER(unqlite), POINTER(POINTER(unqlite_kv_cursor))]
    unqlite_kv_cursor_init.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 829
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_release'):
    unqlite_kv_cursor_release = _libs['unqlite'].unqlite_kv_cursor_release
    unqlite_kv_cursor_release.argtypes = [POINTER(unqlite), POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_release.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 830
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_seek'):
    unqlite_kv_cursor_seek = _libs['unqlite'].unqlite_kv_cursor_seek
    unqlite_kv_cursor_seek.argtypes = [POINTER(unqlite_kv_cursor), POINTER(None), c_int, c_int]
    unqlite_kv_cursor_seek.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 831
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_first_entry'):
    unqlite_kv_cursor_first_entry = _libs['unqlite'].unqlite_kv_cursor_first_entry
    unqlite_kv_cursor_first_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_first_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 832
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_last_entry'):
    unqlite_kv_cursor_last_entry = _libs['unqlite'].unqlite_kv_cursor_last_entry
    unqlite_kv_cursor_last_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_last_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 833
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_valid_entry'):
    unqlite_kv_cursor_valid_entry = _libs['unqlite'].unqlite_kv_cursor_valid_entry
    unqlite_kv_cursor_valid_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_valid_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 834
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_next_entry'):
    unqlite_kv_cursor_next_entry = _libs['unqlite'].unqlite_kv_cursor_next_entry
    unqlite_kv_cursor_next_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_next_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 835
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_prev_entry'):
    unqlite_kv_cursor_prev_entry = _libs['unqlite'].unqlite_kv_cursor_prev_entry
    unqlite_kv_cursor_prev_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_prev_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 836
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_key'):
    unqlite_kv_cursor_key = _libs['unqlite'].unqlite_kv_cursor_key
    unqlite_kv_cursor_key.argtypes = [POINTER(unqlite_kv_cursor), POINTER(None), POINTER(c_int)]
    unqlite_kv_cursor_key.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 837
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_key_callback'):
    unqlite_kv_cursor_key_callback = _libs['unqlite'].unqlite_kv_cursor_key_callback
    unqlite_kv_cursor_key_callback.argtypes = [POINTER(unqlite_kv_cursor), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None)]
    unqlite_kv_cursor_key_callback.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 838
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_data'):
    unqlite_kv_cursor_data = _libs['unqlite'].unqlite_kv_cursor_data
    unqlite_kv_cursor_data.argtypes = [POINTER(unqlite_kv_cursor), POINTER(None), POINTER(unqlite_int64)]
    unqlite_kv_cursor_data.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 839
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_data_callback'):
    unqlite_kv_cursor_data_callback = _libs['unqlite'].unqlite_kv_cursor_data_callback
    unqlite_kv_cursor_data_callback.argtypes = [POINTER(unqlite_kv_cursor), CFUNCTYPE(UNCHECKED(c_int), POINTER(None), c_uint, POINTER(None)), POINTER(None)]
    unqlite_kv_cursor_data_callback.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 840
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_delete_entry'):
    unqlite_kv_cursor_delete_entry = _libs['unqlite'].unqlite_kv_cursor_delete_entry
    unqlite_kv_cursor_delete_entry.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_delete_entry.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 841
if hasattr(_libs['unqlite'], 'unqlite_kv_cursor_reset'):
    unqlite_kv_cursor_reset = _libs['unqlite'].unqlite_kv_cursor_reset
    unqlite_kv_cursor_reset.argtypes = [POINTER(unqlite_kv_cursor)]
    unqlite_kv_cursor_reset.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 844
if hasattr(_libs['unqlite'], 'unqlite_begin'):
    unqlite_begin = _libs['unqlite'].unqlite_begin
    unqlite_begin.argtypes = [POINTER(unqlite)]
    unqlite_begin.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 845
if hasattr(_libs['unqlite'], 'unqlite_commit'):
    unqlite_commit = _libs['unqlite'].unqlite_commit
    unqlite_commit.argtypes = [POINTER(unqlite)]
    unqlite_commit.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 846
if hasattr(_libs['unqlite'], 'unqlite_rollback'):
    unqlite_rollback = _libs['unqlite'].unqlite_rollback
    unqlite_rollback.argtypes = [POINTER(unqlite)]
    unqlite_rollback.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 849
if hasattr(_libs['unqlite'], 'unqlite_util_load_mmaped_file'):
    unqlite_util_load_mmaped_file = _libs['unqlite'].unqlite_util_load_mmaped_file
    unqlite_util_load_mmaped_file.argtypes = [String, POINTER(POINTER(None)), POINTER(unqlite_int64)]
    unqlite_util_load_mmaped_file.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 850
if hasattr(_libs['unqlite'], 'unqlite_util_release_mmaped_file'):
    unqlite_util_release_mmaped_file = _libs['unqlite'].unqlite_util_release_mmaped_file
    unqlite_util_release_mmaped_file.argtypes = [POINTER(None), unqlite_int64]
    unqlite_util_release_mmaped_file.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 851
if hasattr(_libs['unqlite'], 'unqlite_util_random_string'):
    unqlite_util_random_string = _libs['unqlite'].unqlite_util_random_string
    unqlite_util_random_string.argtypes = [POINTER(unqlite), String, c_uint]
    unqlite_util_random_string.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 852
if hasattr(_libs['unqlite'], 'unqlite_util_random_num'):
    unqlite_util_random_num = _libs['unqlite'].unqlite_util_random_num
    unqlite_util_random_num.argtypes = [POINTER(unqlite)]
    unqlite_util_random_num.restype = c_uint

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 855
if hasattr(_libs['unqlite'], 'unqlite_create_function'):
    unqlite_create_function = _libs['unqlite'].unqlite_create_function
    unqlite_create_function.argtypes = [POINTER(unqlite_vm), String, CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_context), c_int, POINTER(POINTER(unqlite_value))), POINTER(None)]
    unqlite_create_function.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 856
if hasattr(_libs['unqlite'], 'unqlite_delete_function'):
    unqlite_delete_function = _libs['unqlite'].unqlite_delete_function
    unqlite_delete_function.argtypes = [POINTER(unqlite_vm), String]
    unqlite_delete_function.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 857
if hasattr(_libs['unqlite'], 'unqlite_create_constant'):
    unqlite_create_constant = _libs['unqlite'].unqlite_create_constant
    unqlite_create_constant.argtypes = [POINTER(unqlite_vm), String, CFUNCTYPE(UNCHECKED(None), POINTER(unqlite_value), POINTER(None)), POINTER(None)]
    unqlite_create_constant.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 858
if hasattr(_libs['unqlite'], 'unqlite_delete_constant'):
    unqlite_delete_constant = _libs['unqlite'].unqlite_delete_constant
    unqlite_delete_constant.argtypes = [POINTER(unqlite_vm), String]
    unqlite_delete_constant.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 861
if hasattr(_libs['unqlite'], 'unqlite_vm_new_scalar'):
    unqlite_vm_new_scalar = _libs['unqlite'].unqlite_vm_new_scalar
    unqlite_vm_new_scalar.argtypes = [POINTER(unqlite_vm)]
    unqlite_vm_new_scalar.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 862
if hasattr(_libs['unqlite'], 'unqlite_vm_new_array'):
    unqlite_vm_new_array = _libs['unqlite'].unqlite_vm_new_array
    unqlite_vm_new_array.argtypes = [POINTER(unqlite_vm)]
    unqlite_vm_new_array.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 863
if hasattr(_libs['unqlite'], 'unqlite_vm_release_value'):
    unqlite_vm_release_value = _libs['unqlite'].unqlite_vm_release_value
    unqlite_vm_release_value.argtypes = [POINTER(unqlite_vm), POINTER(unqlite_value)]
    unqlite_vm_release_value.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 864
if hasattr(_libs['unqlite'], 'unqlite_context_new_scalar'):
    unqlite_context_new_scalar = _libs['unqlite'].unqlite_context_new_scalar
    unqlite_context_new_scalar.argtypes = [POINTER(unqlite_context)]
    unqlite_context_new_scalar.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 865
if hasattr(_libs['unqlite'], 'unqlite_context_new_array'):
    unqlite_context_new_array = _libs['unqlite'].unqlite_context_new_array
    unqlite_context_new_array.argtypes = [POINTER(unqlite_context)]
    unqlite_context_new_array.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 866
if hasattr(_libs['unqlite'], 'unqlite_context_release_value'):
    unqlite_context_release_value = _libs['unqlite'].unqlite_context_release_value
    unqlite_context_release_value.argtypes = [POINTER(unqlite_context), POINTER(unqlite_value)]
    unqlite_context_release_value.restype = None

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 869
if hasattr(_libs['unqlite'], 'unqlite_value_int'):
    unqlite_value_int = _libs['unqlite'].unqlite_value_int
    unqlite_value_int.argtypes = [POINTER(unqlite_value), c_int]
    unqlite_value_int.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 870
if hasattr(_libs['unqlite'], 'unqlite_value_int64'):
    unqlite_value_int64 = _libs['unqlite'].unqlite_value_int64
    unqlite_value_int64.argtypes = [POINTER(unqlite_value), unqlite_int64]
    unqlite_value_int64.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 871
if hasattr(_libs['unqlite'], 'unqlite_value_bool'):
    unqlite_value_bool = _libs['unqlite'].unqlite_value_bool
    unqlite_value_bool.argtypes = [POINTER(unqlite_value), c_int]
    unqlite_value_bool.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 872
if hasattr(_libs['unqlite'], 'unqlite_value_null'):
    unqlite_value_null = _libs['unqlite'].unqlite_value_null
    unqlite_value_null.argtypes = [POINTER(unqlite_value)]
    unqlite_value_null.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 873
if hasattr(_libs['unqlite'], 'unqlite_value_double'):
    unqlite_value_double = _libs['unqlite'].unqlite_value_double
    unqlite_value_double.argtypes = [POINTER(unqlite_value), c_double]
    unqlite_value_double.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 874
if hasattr(_libs['unqlite'], 'unqlite_value_string'):
    unqlite_value_string = _libs['unqlite'].unqlite_value_string
    unqlite_value_string.argtypes = [POINTER(unqlite_value), String, c_int]
    unqlite_value_string.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 875
if hasattr(_libs['unqlite'], 'unqlite_value_string_format'):
    _func = _libs['unqlite'].unqlite_value_string_format
    _restype = c_int
    _argtypes = [POINTER(unqlite_value), String]
    unqlite_value_string_format = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 876
if hasattr(_libs['unqlite'], 'unqlite_value_reset_string_cursor'):
    unqlite_value_reset_string_cursor = _libs['unqlite'].unqlite_value_reset_string_cursor
    unqlite_value_reset_string_cursor.argtypes = [POINTER(unqlite_value)]
    unqlite_value_reset_string_cursor.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 877
if hasattr(_libs['unqlite'], 'unqlite_value_resource'):
    unqlite_value_resource = _libs['unqlite'].unqlite_value_resource
    unqlite_value_resource.argtypes = [POINTER(unqlite_value), POINTER(None)]
    unqlite_value_resource.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 878
if hasattr(_libs['unqlite'], 'unqlite_value_release'):
    unqlite_value_release = _libs['unqlite'].unqlite_value_release
    unqlite_value_release.argtypes = [POINTER(unqlite_value)]
    unqlite_value_release.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 881
if hasattr(_libs['unqlite'], 'unqlite_value_to_int'):
    unqlite_value_to_int = _libs['unqlite'].unqlite_value_to_int
    unqlite_value_to_int.argtypes = [POINTER(unqlite_value)]
    unqlite_value_to_int.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 882
if hasattr(_libs['unqlite'], 'unqlite_value_to_bool'):
    unqlite_value_to_bool = _libs['unqlite'].unqlite_value_to_bool
    unqlite_value_to_bool.argtypes = [POINTER(unqlite_value)]
    unqlite_value_to_bool.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 883
if hasattr(_libs['unqlite'], 'unqlite_value_to_int64'):
    unqlite_value_to_int64 = _libs['unqlite'].unqlite_value_to_int64
    unqlite_value_to_int64.argtypes = [POINTER(unqlite_value)]
    unqlite_value_to_int64.restype = unqlite_int64

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 884
if hasattr(_libs['unqlite'], 'unqlite_value_to_double'):
    unqlite_value_to_double = _libs['unqlite'].unqlite_value_to_double
    unqlite_value_to_double.argtypes = [POINTER(unqlite_value)]
    unqlite_value_to_double.restype = c_double

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 885
if hasattr(_libs['unqlite'], 'unqlite_value_to_string'):
    unqlite_value_to_string = _libs['unqlite'].unqlite_value_to_string
    unqlite_value_to_string.argtypes = [POINTER(unqlite_value), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_value_to_string.restype = ReturnString
    else:
        unqlite_value_to_string.restype = String
        unqlite_value_to_string.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 886
if hasattr(_libs['unqlite'], 'unqlite_value_to_resource'):
    unqlite_value_to_resource = _libs['unqlite'].unqlite_value_to_resource
    unqlite_value_to_resource.argtypes = [POINTER(unqlite_value)]
    unqlite_value_to_resource.restype = POINTER(None)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 887
if hasattr(_libs['unqlite'], 'unqlite_value_compare'):
    unqlite_value_compare = _libs['unqlite'].unqlite_value_compare
    unqlite_value_compare.argtypes = [POINTER(unqlite_value), POINTER(unqlite_value), c_int]
    unqlite_value_compare.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 890
if hasattr(_libs['unqlite'], 'unqlite_result_int'):
    unqlite_result_int = _libs['unqlite'].unqlite_result_int
    unqlite_result_int.argtypes = [POINTER(unqlite_context), c_int]
    unqlite_result_int.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 891
if hasattr(_libs['unqlite'], 'unqlite_result_int64'):
    unqlite_result_int64 = _libs['unqlite'].unqlite_result_int64
    unqlite_result_int64.argtypes = [POINTER(unqlite_context), unqlite_int64]
    unqlite_result_int64.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 892
if hasattr(_libs['unqlite'], 'unqlite_result_bool'):
    unqlite_result_bool = _libs['unqlite'].unqlite_result_bool
    unqlite_result_bool.argtypes = [POINTER(unqlite_context), c_int]
    unqlite_result_bool.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 893
if hasattr(_libs['unqlite'], 'unqlite_result_double'):
    unqlite_result_double = _libs['unqlite'].unqlite_result_double
    unqlite_result_double.argtypes = [POINTER(unqlite_context), c_double]
    unqlite_result_double.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 894
if hasattr(_libs['unqlite'], 'unqlite_result_null'):
    unqlite_result_null = _libs['unqlite'].unqlite_result_null
    unqlite_result_null.argtypes = [POINTER(unqlite_context)]
    unqlite_result_null.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 895
if hasattr(_libs['unqlite'], 'unqlite_result_string'):
    unqlite_result_string = _libs['unqlite'].unqlite_result_string
    unqlite_result_string.argtypes = [POINTER(unqlite_context), String, c_int]
    unqlite_result_string.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 896
if hasattr(_libs['unqlite'], 'unqlite_result_string_format'):
    _func = _libs['unqlite'].unqlite_result_string_format
    _restype = c_int
    _argtypes = [POINTER(unqlite_context), String]
    unqlite_result_string_format = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 897
if hasattr(_libs['unqlite'], 'unqlite_result_value'):
    unqlite_result_value = _libs['unqlite'].unqlite_result_value
    unqlite_result_value.argtypes = [POINTER(unqlite_context), POINTER(unqlite_value)]
    unqlite_result_value.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 898
if hasattr(_libs['unqlite'], 'unqlite_result_resource'):
    unqlite_result_resource = _libs['unqlite'].unqlite_result_resource
    unqlite_result_resource.argtypes = [POINTER(unqlite_context), POINTER(None)]
    unqlite_result_resource.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 901
if hasattr(_libs['unqlite'], 'unqlite_value_is_int'):
    unqlite_value_is_int = _libs['unqlite'].unqlite_value_is_int
    unqlite_value_is_int.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_int.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 902
if hasattr(_libs['unqlite'], 'unqlite_value_is_float'):
    unqlite_value_is_float = _libs['unqlite'].unqlite_value_is_float
    unqlite_value_is_float.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_float.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 903
if hasattr(_libs['unqlite'], 'unqlite_value_is_bool'):
    unqlite_value_is_bool = _libs['unqlite'].unqlite_value_is_bool
    unqlite_value_is_bool.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_bool.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 904
if hasattr(_libs['unqlite'], 'unqlite_value_is_string'):
    unqlite_value_is_string = _libs['unqlite'].unqlite_value_is_string
    unqlite_value_is_string.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_string.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 905
if hasattr(_libs['unqlite'], 'unqlite_value_is_null'):
    unqlite_value_is_null = _libs['unqlite'].unqlite_value_is_null
    unqlite_value_is_null.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_null.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 906
if hasattr(_libs['unqlite'], 'unqlite_value_is_numeric'):
    unqlite_value_is_numeric = _libs['unqlite'].unqlite_value_is_numeric
    unqlite_value_is_numeric.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_numeric.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 907
if hasattr(_libs['unqlite'], 'unqlite_value_is_callable'):
    unqlite_value_is_callable = _libs['unqlite'].unqlite_value_is_callable
    unqlite_value_is_callable.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_callable.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 908
if hasattr(_libs['unqlite'], 'unqlite_value_is_scalar'):
    unqlite_value_is_scalar = _libs['unqlite'].unqlite_value_is_scalar
    unqlite_value_is_scalar.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_scalar.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 909
if hasattr(_libs['unqlite'], 'unqlite_value_is_json_array'):
    unqlite_value_is_json_array = _libs['unqlite'].unqlite_value_is_json_array
    unqlite_value_is_json_array.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_json_array.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 910
if hasattr(_libs['unqlite'], 'unqlite_value_is_json_object'):
    unqlite_value_is_json_object = _libs['unqlite'].unqlite_value_is_json_object
    unqlite_value_is_json_object.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_json_object.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 911
if hasattr(_libs['unqlite'], 'unqlite_value_is_resource'):
    unqlite_value_is_resource = _libs['unqlite'].unqlite_value_is_resource
    unqlite_value_is_resource.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_resource.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 912
if hasattr(_libs['unqlite'], 'unqlite_value_is_empty'):
    unqlite_value_is_empty = _libs['unqlite'].unqlite_value_is_empty
    unqlite_value_is_empty.argtypes = [POINTER(unqlite_value)]
    unqlite_value_is_empty.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 915
if hasattr(_libs['unqlite'], 'unqlite_array_fetch'):
    unqlite_array_fetch = _libs['unqlite'].unqlite_array_fetch
    unqlite_array_fetch.argtypes = [POINTER(unqlite_value), String, c_int]
    unqlite_array_fetch.restype = POINTER(unqlite_value)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 916
if hasattr(_libs['unqlite'], 'unqlite_array_walk'):
    unqlite_array_walk = _libs['unqlite'].unqlite_array_walk
    unqlite_array_walk.argtypes = [POINTER(unqlite_value), CFUNCTYPE(UNCHECKED(c_int), POINTER(unqlite_value), POINTER(unqlite_value), POINTER(None)), POINTER(None)]
    unqlite_array_walk.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 917
if hasattr(_libs['unqlite'], 'unqlite_array_add_elem'):
    unqlite_array_add_elem = _libs['unqlite'].unqlite_array_add_elem
    unqlite_array_add_elem.argtypes = [POINTER(unqlite_value), POINTER(unqlite_value), POINTER(unqlite_value)]
    unqlite_array_add_elem.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 918
if hasattr(_libs['unqlite'], 'unqlite_array_add_strkey_elem'):
    unqlite_array_add_strkey_elem = _libs['unqlite'].unqlite_array_add_strkey_elem
    unqlite_array_add_strkey_elem.argtypes = [POINTER(unqlite_value), String, POINTER(unqlite_value)]
    unqlite_array_add_strkey_elem.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 919
if hasattr(_libs['unqlite'], 'unqlite_array_count'):
    unqlite_array_count = _libs['unqlite'].unqlite_array_count
    unqlite_array_count.argtypes = [POINTER(unqlite_value)]
    unqlite_array_count.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 922
if hasattr(_libs['unqlite'], 'unqlite_context_output'):
    unqlite_context_output = _libs['unqlite'].unqlite_context_output
    unqlite_context_output.argtypes = [POINTER(unqlite_context), String, c_int]
    unqlite_context_output.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 923
if hasattr(_libs['unqlite'], 'unqlite_context_output_format'):
    _func = _libs['unqlite'].unqlite_context_output_format
    _restype = c_int
    _argtypes = [POINTER(unqlite_context), String]
    unqlite_context_output_format = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 924
if hasattr(_libs['unqlite'], 'unqlite_context_throw_error'):
    unqlite_context_throw_error = _libs['unqlite'].unqlite_context_throw_error
    unqlite_context_throw_error.argtypes = [POINTER(unqlite_context), c_int, String]
    unqlite_context_throw_error.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 925
if hasattr(_libs['unqlite'], 'unqlite_context_throw_error_format'):
    _func = _libs['unqlite'].unqlite_context_throw_error_format
    _restype = c_int
    _argtypes = [POINTER(unqlite_context), c_int, String]
    unqlite_context_throw_error_format = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 926
if hasattr(_libs['unqlite'], 'unqlite_context_random_num'):
    unqlite_context_random_num = _libs['unqlite'].unqlite_context_random_num
    unqlite_context_random_num.argtypes = [POINTER(unqlite_context)]
    unqlite_context_random_num.restype = c_uint

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 927
if hasattr(_libs['unqlite'], 'unqlite_context_random_string'):
    unqlite_context_random_string = _libs['unqlite'].unqlite_context_random_string
    unqlite_context_random_string.argtypes = [POINTER(unqlite_context), String, c_int]
    unqlite_context_random_string.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 928
if hasattr(_libs['unqlite'], 'unqlite_context_user_data'):
    unqlite_context_user_data = _libs['unqlite'].unqlite_context_user_data
    unqlite_context_user_data.argtypes = [POINTER(unqlite_context)]
    unqlite_context_user_data.restype = POINTER(None)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 929
if hasattr(_libs['unqlite'], 'unqlite_context_push_aux_data'):
    unqlite_context_push_aux_data = _libs['unqlite'].unqlite_context_push_aux_data
    unqlite_context_push_aux_data.argtypes = [POINTER(unqlite_context), POINTER(None)]
    unqlite_context_push_aux_data.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 930
if hasattr(_libs['unqlite'], 'unqlite_context_peek_aux_data'):
    unqlite_context_peek_aux_data = _libs['unqlite'].unqlite_context_peek_aux_data
    unqlite_context_peek_aux_data.argtypes = [POINTER(unqlite_context)]
    unqlite_context_peek_aux_data.restype = POINTER(None)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 931
if hasattr(_libs['unqlite'], 'unqlite_context_result_buf_length'):
    unqlite_context_result_buf_length = _libs['unqlite'].unqlite_context_result_buf_length
    unqlite_context_result_buf_length.argtypes = [POINTER(unqlite_context)]
    unqlite_context_result_buf_length.restype = c_uint

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 932
if hasattr(_libs['unqlite'], 'unqlite_function_name'):
    unqlite_function_name = _libs['unqlite'].unqlite_function_name
    unqlite_function_name.argtypes = [POINTER(unqlite_context)]
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_function_name.restype = ReturnString
    else:
        unqlite_function_name.restype = String
        unqlite_function_name.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 935
if hasattr(_libs['unqlite'], 'unqlite_context_alloc_chunk'):
    unqlite_context_alloc_chunk = _libs['unqlite'].unqlite_context_alloc_chunk
    unqlite_context_alloc_chunk.argtypes = [POINTER(unqlite_context), c_uint, c_int, c_int]
    unqlite_context_alloc_chunk.restype = POINTER(None)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 936
if hasattr(_libs['unqlite'], 'unqlite_context_realloc_chunk'):
    unqlite_context_realloc_chunk = _libs['unqlite'].unqlite_context_realloc_chunk
    unqlite_context_realloc_chunk.argtypes = [POINTER(unqlite_context), POINTER(None), c_uint]
    unqlite_context_realloc_chunk.restype = POINTER(None)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 937
if hasattr(_libs['unqlite'], 'unqlite_context_free_chunk'):
    unqlite_context_free_chunk = _libs['unqlite'].unqlite_context_free_chunk
    unqlite_context_free_chunk.argtypes = [POINTER(unqlite_context), POINTER(None)]
    unqlite_context_free_chunk.restype = None

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 940
if hasattr(_libs['unqlite'], 'unqlite_lib_config'):
    _func = _libs['unqlite'].unqlite_lib_config
    _restype = c_int
    _argtypes = [c_int]
    unqlite_lib_config = _variadic_function(_func,_restype,_argtypes)

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 941
if hasattr(_libs['unqlite'], 'unqlite_lib_init'):
    unqlite_lib_init = _libs['unqlite'].unqlite_lib_init
    unqlite_lib_init.argtypes = []
    unqlite_lib_init.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 942
if hasattr(_libs['unqlite'], 'unqlite_lib_shutdown'):
    unqlite_lib_shutdown = _libs['unqlite'].unqlite_lib_shutdown
    unqlite_lib_shutdown.argtypes = []
    unqlite_lib_shutdown.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 943
if hasattr(_libs['unqlite'], 'unqlite_lib_is_threadsafe'):
    unqlite_lib_is_threadsafe = _libs['unqlite'].unqlite_lib_is_threadsafe
    unqlite_lib_is_threadsafe.argtypes = []
    unqlite_lib_is_threadsafe.restype = c_int

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 944
if hasattr(_libs['unqlite'], 'unqlite_lib_version'):
    unqlite_lib_version = _libs['unqlite'].unqlite_lib_version
    unqlite_lib_version.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_lib_version.restype = ReturnString
    else:
        unqlite_lib_version.restype = String
        unqlite_lib_version.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 945
if hasattr(_libs['unqlite'], 'unqlite_lib_signature'):
    unqlite_lib_signature = _libs['unqlite'].unqlite_lib_signature
    unqlite_lib_signature.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_lib_signature.restype = ReturnString
    else:
        unqlite_lib_signature.restype = String
        unqlite_lib_signature.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 946
if hasattr(_libs['unqlite'], 'unqlite_lib_ident'):
    unqlite_lib_ident = _libs['unqlite'].unqlite_lib_ident
    unqlite_lib_ident.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_lib_ident.restype = ReturnString
    else:
        unqlite_lib_ident.restype = String
        unqlite_lib_ident.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 947
if hasattr(_libs['unqlite'], 'unqlite_lib_copyright'):
    unqlite_lib_copyright = _libs['unqlite'].unqlite_lib_copyright
    unqlite_lib_copyright.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        unqlite_lib_copyright.restype = ReturnString
    else:
        unqlite_lib_copyright.restype = String
        unqlite_lib_copyright.errcheck = ReturnString

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 57
try:
    UNQLITE_VERSION = '1.1.6'
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 63
try:
    UNQLITE_VERSION_NUMBER = 1001006
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 71
try:
    UNQLITE_SIG = 'unqlite/1.1.6'
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 78
try:
    UNQLITE_IDENT = 'unqlite:b172a1e2c3f62fb35c8e1fb2795121f82356cad6'
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 88
try:
    UNQLITE_COPYRIGHT = 'Copyright (C) Symisc Systems, S.U.A.R.L [Mrad Chems Eddine <chm@symisc.net>] 2012-2013, http://unqlite.org/'
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 295
try:
    SXRET_OK = 0
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 296
try:
    SXERR_MEM = (-1)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 297
try:
    SXERR_IO = (-2)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 298
try:
    SXERR_EMPTY = (-3)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 299
try:
    SXERR_LOCKED = (-4)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 300
try:
    SXERR_ORANGE = (-5)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 301
try:
    SXERR_NOTFOUND = (-6)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 302
try:
    SXERR_LIMIT = (-7)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 303
try:
    SXERR_MORE = (-8)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 304
try:
    SXERR_INVALID = (-9)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 305
try:
    SXERR_ABORT = (-10)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 306
try:
    SXERR_EXISTS = (-11)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 307
try:
    SXERR_SYNTAX = (-12)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 308
try:
    SXERR_UNKNOWN = (-13)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 309
try:
    SXERR_BUSY = (-14)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 310
try:
    SXERR_OVERFLOW = (-15)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 311
try:
    SXERR_WILLBLOCK = (-16)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 312
try:
    SXERR_NOTIMPLEMENTED = (-17)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 313
try:
    SXERR_EOF = (-18)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 314
try:
    SXERR_PERM = (-19)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 315
try:
    SXERR_NOOP = (-20)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 316
try:
    SXERR_FORMAT = (-21)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 317
try:
    SXERR_NEXT = (-22)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 318
try:
    SXERR_OS = (-23)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 319
try:
    SXERR_CORRUPT = (-24)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 320
try:
    SXERR_CONTINUE = (-25)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 321
try:
    SXERR_NOMATCH = (-26)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 322
try:
    SXERR_RESET = (-27)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 323
try:
    SXERR_DONE = (-28)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 324
try:
    SXERR_SHORT = (-29)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 325
try:
    SXERR_PATH = (-30)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 326
try:
    SXERR_TIMEOUT = (-31)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 327
try:
    SXERR_BIG = (-32)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 328
try:
    SXERR_RETRY = (-33)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 329
try:
    SXERR_IGNORE = (-63)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 346
try:
    UNQLITE_OK = SXRET_OK
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 348
try:
    UNQLITE_NOMEM = SXERR_MEM
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 349
try:
    UNQLITE_ABORT = SXERR_ABORT
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 350
try:
    UNQLITE_IOERR = SXERR_IO
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 351
try:
    UNQLITE_CORRUPT = SXERR_CORRUPT
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 352
try:
    UNQLITE_LOCKED = SXERR_LOCKED
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 353
try:
    UNQLITE_BUSY = SXERR_BUSY
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 354
try:
    UNQLITE_DONE = SXERR_DONE
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 355
try:
    UNQLITE_PERM = SXERR_PERM
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 356
try:
    UNQLITE_NOTIMPLEMENTED = SXERR_NOTIMPLEMENTED
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 357
try:
    UNQLITE_NOTFOUND = SXERR_NOTFOUND
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 358
try:
    UNQLITE_NOOP = SXERR_NOOP
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 359
try:
    UNQLITE_INVALID = SXERR_INVALID
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 360
try:
    UNQLITE_EOF = SXERR_EOF
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 361
try:
    UNQLITE_UNKNOWN = SXERR_UNKNOWN
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 362
try:
    UNQLITE_LIMIT = SXERR_LIMIT
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 363
try:
    UNQLITE_EXISTS = SXERR_EXISTS
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 364
try:
    UNQLITE_EMPTY = SXERR_EMPTY
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 365
try:
    UNQLITE_COMPILE_ERR = (-70)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 366
try:
    UNQLITE_VM_ERR = (-71)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 367
try:
    UNQLITE_FULL = (-73)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 368
try:
    UNQLITE_CANTOPEN = (-74)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 369
try:
    UNQLITE_READ_ONLY = (-75)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 370
try:
    UNQLITE_LOCKERR = (-76)
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 386
try:
    UNQLITE_CONFIG_JX9_ERR_LOG = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 387
try:
    UNQLITE_CONFIG_MAX_PAGE_CACHE = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 388
try:
    UNQLITE_CONFIG_ERR_LOG = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 389
try:
    UNQLITE_CONFIG_KV_ENGINE = 4
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 390
try:
    UNQLITE_CONFIG_DISABLE_AUTO_COMMIT = 5
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 391
try:
    UNQLITE_CONFIG_GET_KV_NAME = 6
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 409
try:
    UNQLITE_VM_CONFIG_OUTPUT = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 410
try:
    UNQLITE_VM_CONFIG_IMPORT_PATH = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 411
try:
    UNQLITE_VM_CONFIG_ERR_REPORT = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 412
try:
    UNQLITE_VM_CONFIG_RECURSION_DEPTH = 4
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 413
try:
    UNQLITE_VM_OUTPUT_LENGTH = 5
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 414
try:
    UNQLITE_VM_CONFIG_CREATE_VAR = 6
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 415
try:
    UNQLITE_VM_CONFIG_HTTP_REQUEST = 7
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 416
try:
    UNQLITE_VM_CONFIG_SERVER_ATTR = 8
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 417
try:
    UNQLITE_VM_CONFIG_ENV_ATTR = 9
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 418
try:
    UNQLITE_VM_CONFIG_EXEC_VALUE = 10
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 419
try:
    UNQLITE_VM_CONFIG_IO_STREAM = 11
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 420
try:
    UNQLITE_VM_CONFIG_ARGV_ENTRY = 12
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 421
try:
    UNQLITE_VM_CONFIG_EXTRACT_OUTPUT = 13
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 435
try:
    UNQLITE_KV_CONFIG_HASH_FUNC = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 436
try:
    UNQLITE_KV_CONFIG_CMP_FUNC = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 461
try:
    UNQLITE_LIB_CONFIG_USER_MALLOC = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 462
try:
    UNQLITE_LIB_CONFIG_MEM_ERR_CALLBACK = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 463
try:
    UNQLITE_LIB_CONFIG_USER_MUTEX = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 464
try:
    UNQLITE_LIB_CONFIG_THREAD_LEVEL_SINGLE = 4
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 465
try:
    UNQLITE_LIB_CONFIG_THREAD_LEVEL_MULTI = 5
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 466
try:
    UNQLITE_LIB_CONFIG_VFS = 6
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 467
try:
    UNQLITE_LIB_CONFIG_STORAGE_ENGINE = 7
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 468
try:
    UNQLITE_LIB_CONFIG_PAGE_SIZE = 8
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 473
try:
    UNQLITE_OPEN_READONLY = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 474
try:
    UNQLITE_OPEN_READWRITE = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 475
try:
    UNQLITE_OPEN_CREATE = 4
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 476
try:
    UNQLITE_OPEN_EXCLUSIVE = 8
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 477
try:
    UNQLITE_OPEN_TEMP_DB = 16
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 478
try:
    UNQLITE_OPEN_NOMUTEX = 32
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 479
try:
    UNQLITE_OPEN_OMIT_JOURNALING = 64
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 480
try:
    UNQLITE_OPEN_IN_MEMORY = 128
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 481
try:
    UNQLITE_OPEN_MMAP = 256
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 494
try:
    UNQLITE_SYNC_NORMAL = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 495
try:
    UNQLITE_SYNC_FULL = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 496
try:
    UNQLITE_SYNC_DATAONLY = 16
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 504
try:
    UNQLITE_LOCK_NONE = 0
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 505
try:
    UNQLITE_LOCK_SHARED = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 506
try:
    UNQLITE_LOCK_RESERVED = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 507
try:
    UNQLITE_LOCK_PENDING = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 508
try:
    UNQLITE_LOCK_EXCLUSIVE = 4
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 643
try:
    UNQLITE_ACCESS_EXISTS = 0
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 644
try:
    UNQLITE_ACCESS_READWRITE = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 645
try:
    UNQLITE_ACCESS_READ = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 712
try:
    UNQLITE_CURSOR_MATCH_EXACT = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 713
try:
    UNQLITE_CURSOR_MATCH_LE = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 714
try:
    UNQLITE_CURSOR_MATCH_GE = 3
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 783
try:
    UNQLITE_JOURNAL_FILE_SUFFIX = '_unqlite_journal'
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 793
try:
    UNQLITE_CTX_ERR = 1
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 794
try:
    UNQLITE_CTX_WARNING = 2
except:
    pass

# /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 795
try:
    UNQLITE_CTX_NOTICE = 3
except:
    pass

unqlite_io_methods = struct_unqlite_io_methods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 563

unqlite_kv_methods = struct_unqlite_kv_methods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 743

unqlite_kv_engine = struct_unqlite_kv_engine # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 730

jx9_io_stream = struct_jx9_io_stream # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 94

jx9_context = struct_jx9_context # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 95

jx9_value = struct_jx9_value # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 96

unqlite_vfs = struct_unqlite_vfs # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 609

unqlite_vm = struct_unqlite_vm # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 98

unqlite = struct_unqlite # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 99

SyMutexMethods = struct_SyMutexMethods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 277

SyMemMethods = struct_SyMemMethods # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 264

SyString = struct_SyString # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 215

syiovec = struct_syiovec # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 204

SyMutex = struct_SyMutex # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 201

Sytm = struct_Sytm # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 221

unqlite_file = struct_unqlite_file # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 520

unqlite_page = struct_unqlite_page # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 657

unqlite_kv_io = struct_unqlite_kv_io # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 674

unqlite_kv_cursor = struct_unqlite_kv_cursor # /Users/nobo/Dropbox/Projects/unqlitepy/unqlite.h: 704

# No inserted files

