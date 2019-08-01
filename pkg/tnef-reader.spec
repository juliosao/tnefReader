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
Requires: tnef python-gi


%description
Utility for view content of Tnef files like Winmail.dat

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/%name/mime

cp -rf src/* $RPM_BUILD_ROOT/opt/%name
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
cp extras/tnef-reader.desktop $RPM_BUILD_ROOT/usr/share/applications
cp extras/tnef-reader.svg $RPM_BUILD_ROOT/opt/%name

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
/opt/tnef-reader/ui/guardar.glade
/usr/share/applications/tnef-reader.desktop

%changelog

* Thu Aug 2 2019 Julio A. García López <juliosao@gmail.com> 0.1
- Initial (And incomplete) package


		
