
CC=gcc
PLATFORM=$(shell uname)
ifeq ($(PLATFORM),Darwin)
LINKOPT=
OUTPUTLIB=libunqlite.dylib
else
LINKOPT=-Wl,-soname,libunqlite.so.1
OUTPUTLIB=libunqlite.so.1.0
endif

.PHONY: all build clean

all: build

clean:
	-rm _unqlite.py
	-rm $(OUTPUTLIB)

build: _unqlite.py

$(OUTPUTLIB): unqlite.h unqlite.c
	$(CC) -DUNQLITE_ENABLE_THREADS=1 -Wall -fPIC -c unqlite.c
	$(CC) -shared $(LINKOPT) -o $(OUTPUTLIB) unqlite.o

_unqlite.py: $(OUTPUTLIB)
	ctypesgen.py unqlite.h -L ./ -l unqlite -o _unqlite.py
