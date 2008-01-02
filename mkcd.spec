%define name mkcd
%define version 4.2.6
%define release %mkrel 1
%define _requires_exceptions perl(strict)
%define _provides_exceptions perl(install_any)

Summary: Script to build Linux distributions installation discs
Name: %{name}
Version: %{version}
Release: %{release}
# get the source from our cvs repository (see
# http://cvs.mandriva.com/)
Source0: %{name}-%{version}.tar.bz2
License: GPL
url: http://people.mandriva.com/~warly/files/mkcd/
Group: System/Configuration/Packaging
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Requires: perl-File-NCopy perl-Image-Size perl-URPM
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
%doc README
%{_bindir}/*
%{perl_vendorlib}/Mkcd


