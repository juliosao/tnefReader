TARGET=tnef-reader
VERSION=$(shell awk '/Version:/ { print $$2 }' $(TARGET).spec)
COMPANY=aldeasa
DIST=Makefile $(TARGET).spec ./compila-traducciones.sh ./actualiza-traducciones.sh src extras

.phony: pkg clean install locales all 

all: locales 

$(TARGET)-$(VERSION).tar.bz2: clean
	mkdir $(TARGET)-$(VERSION)
	cp -r $(DIST) $(TARGET)-$(VERSION)
	tar cvjf $(TARGET)-$(VERSION).tar.bz2 $(TARGET)-$(VERSION) --exclude=".svn" --exclude="*.pyc" --exclude="*.pyo"
	rm -rf $(TARGET)-$(VERSION)

locales:
	touch ./compila-traducciones.sh

pkg: 	$(TARGET)-$(VERSION).tar.bz2

rpm:  	$(TARGET)-$(VERSION).tar.bz2
	rpmbuild -tb $(TARGET)-$(VERSION).tar.bz2


clean:
	find . -name '*.pyc' -not -iwholename '*.svn*' -exec rm -f {} \;
	find . -name '*~' -not -iwholename '*.svn*' -exec rm -f {} \;
	rm -rf src/translations/??/LC_MESSAGES

	-rm -rf $(TARGET)-$(VERSION)
	-rm -f $(TARGET)-$(VERSION).tar.bz2

