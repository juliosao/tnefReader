%define compatible 1
Summary: Tnef reader GUI
Name: tnef-reader
Version: 0.1
Release: 1%{?dist}
URL: https://github.com/juliosao/tnefReader
License: GPLv3
ExclusiveOS: Linux
Group: Network
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Source0: %{name}-%{version}.tar.bz2
Requires: tnef python-gobject


%description
Utility for view content of Tnef files like Winmail.dat

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post
update-desktop-database

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(444,root,root,555)
%attr(555,root,root)/opt/tnef-reader/TnefReader.py
/opt/tnef-reader/tnef-reader.svg
/opt/tnef-reader/TnefReader.pyc
/opt/tnef-reader/TnefReader.pyo
/opt/tnef-reader/tnefmgr.py
/opt/tnef-reader/tnefmgr.pyc
/opt/tnef-reader/tnefmgr.pyo
/opt/tnef-reader/ui/main.glade
/usr/share/applications/tnef-reader.desktop

%changelog

* Fri Aug 2 2019 Julio A. García López <juliosao@gmail.com> 0.1
- Initial (And incomplete) package


		
