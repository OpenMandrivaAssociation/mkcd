%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl(strict)'
%define __noautoprov 'perl(install_any)'
%else
%define _requires_exceptions perl(strict)
%define _provides_exceptions perl(install_any)
%endif

Summary:	Script to build %{distribution} distributions installation discs
Name:		mkcd
Version:	4.3.0
Release:	9
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/mkcd/
Group:		System/Configuration/Packaging
Requires:	perl-File-NCopy perl-Image-Size perl-URPM packdrake
Requires:	isolinux rpmtools
Suggests:	gfxboot mandriva-theme rosa-gfxboot-theme
Suggests:	drakx-installer-stage2 drakx-installer-advertising drakx-installer-binaries
BuildArch:	noarch
BuildRequires:	libxslt-proc

%description
mkcd script eases the packages repartition over CDs, 
allows to order packages and to create discs of any 
given size (CDs, DVDs...)

%prep
%setup -q

%build

%install
make install PREFIX=%{buildroot}

%files
%defattr(-,root,root)
%doc README doc/
%{_bindir}/*
%{perl_vendorlib}/Mkcd
