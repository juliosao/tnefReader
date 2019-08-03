# tnefReader
A tnef / Winmail.dat reader for Linux

This project aims to be a graphical interface to open winmail.dat files generated with outlook.

## Use
- execute TnefReader.py with winmail.dat file as argument

## Install
- Make sure you have tnef and python-gi installed
- Go into project folder
- Execute "make install" (without the quotes)
- Execute update-desktop-database

## Uninstall
- Go into project folder
- Execute "make uninstall" (without the quotes)

## Making installer
### Debian, Ubuntu, Mint...
- Go into project folder
- Execute "make deb" (without the quotes)
- The installer package is created at current directory

### Redhat, Centos, Fedora...
- Go into project folder
- Execute "make rpm" (without the quotes)
- The installer package package is created where rpmbuild is configured (Per example ~/rpmbuild/RPMS)

