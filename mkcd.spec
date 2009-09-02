%define name mkcd
%define version 4.3.0
%define release %mkrel 3
%define _requires_exceptions perl(strict)
%define _provides_exceptions perl(install_any)

Summary: Script to build Mandriva Linux distributions installation discs
Name: %{name}
Version: %{version}
Release: %{release}
# get the source from our svn repository
# svn.mandriva.com/build_system/mkcd/
Source0: %{name}-%{version}.tar.bz2
License: GPL
URL: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/mkcd/
Group: System/Configuration/Packaging
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Requires: perl-File-NCopy perl-Image-Size perl-URPM packdrake
requires: mandriva-theme isolinux gfxboot rpmtools mandriva-gfxboot-theme
requires: drakx-installer-stage2 drakx-installer-advertising drakx-installer-binaries
BuildArch: noarch
BuildRequires: libxslt-proc

%description
mkcd script eases the packages repartition over CDs, 
allows to order packages and to create discs of any 
given size (CDs, DVDs...)

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/
%{_bindir}/*
%{perl_vendorlib}/Mkcd
