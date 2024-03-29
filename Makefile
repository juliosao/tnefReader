TARGET=tnef-reader
VERSION=0.1
COMPANY=aldeasa
DIST=Makefile src extras pkg


.phony: pkg clean install locales all 

$(TARGET)-$(VERSION).tar.bz2: clean
	mkdir $(TARGET)-$(VERSION)
	cp -r $(DIST) $(TARGET)-$(VERSION)
	sed -i "s/VERSION/$(VERSION)/g" $(TARGET)-$(VERSION)/pkg/tnef-reader.spec
	tar --exclude=".svn" --exclude="*.pyc" --exclude="*.pyo" -cvjf $(TARGET)-$(VERSION).tar.bz2 $(TARGET)-$(VERSION)
	rm -rf $(TARGET)-$(VERSION)

pkg: $(TARGET)-$(VERSION)

rpm: $(TARGET)-$(VERSION).tar.bz2
	rpmbuild -tb $(TARGET)-$(VERSION).tar.bz2

deb:
	make install DESTDIR=$(TARGET)-$(VERSION)
	cp -r pkg/DEBIAN $(TARGET)-$(VERSION)
	sed -i "s/VERSION/$(VERSION)/g" $(TARGET)-$(VERSION)/DEBIAN/control
	dpkg-deb --build $(TARGET)-$(VERSION)

install: clean
	mkdir -p $(DESTDIR)/opt/tnef-reader
	mkdir -p $(DESTDIR)/usr/share/applications
	cp -r src/* $(DESTDIR)/opt/tnef-reader
	cp extras/tnef-reader.desktop $(DESTDIR)/usr/share/applications
	cp extras/tnef-reader.svg $(DESTDIR)/opt/tnef-reader

uninstall:
	-rm -rf $(DESTDIR)/opt/tnef-reader
	-rf -f $(DESTDIR)/usr/share/applications/tnef-reader.desktop
	-rm -f $(DESTDIR)/opt/tnef-reader/tnef-reader.svg

clean:
	find . -name '*.pyc' -not -iwholename '*.svn*' -exec rm -f {} \;
	find . -name '*~' -not -iwholename '*.svn*' -exec rm -f {} \;
	rm -rf src/translations/??/LC_MESSAGES
	-rm -f $(TARGET)-$(VERSION).deb
	-rm -rf $(TARGET)-$(VERSION)
	-rm -f $(TARGET)-$(VERSION).tar.bz2

