include config.mk

EXE = clpy.py

all:

install: $(EXE)
	mkdir -p $(PREFIX)/bin/
	install $(EXE) $(PREFIX)/bin/$(basename $(EXE))

uninstall:
	rm -f $(PREFIX)/bin/$(basename $(EXE))


.PHONY: all install uninstall
