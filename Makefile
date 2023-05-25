include config.mk

EXE = clpy.py
DIR = $(DESTDIR)$(PREFIX)/bin/

all:
	sed 's/^VERSION =.*$$/VERSION = "$(VERSION)"/' clpy.py -i

install: all
	@mkdir -p $(DIR)
	install $(EXE) $(DIR)/$(basename $(EXE))

uninstall:
	rm -f $(DIR)/$(basename $(EXE))


.PHONY: all install uninstall
