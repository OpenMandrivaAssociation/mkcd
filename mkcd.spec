%define name mkcd
%define version 4.3.0
%define release 7

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl(strict)'
%define __noautoprov 'perl(install_any)'
%else
%define _requires_exceptions perl(strict)
%define _provides_exceptions perl(install_any)
%endif

Summary:	Script to build ROSA Linux distributions installation discs
Name:		%{name}
Version:	%{version}
Release:	%{release}
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


%changelog
* Wed May 19 2010 Olivier Blin <oblin@mandriva.com> 4.3.0-6mdv2010.1
+ Revision: 545318
- suggest gfxboot instead of requiring it (not available on ARM/MIPS)

* Thu Mar 18 2010 Olivier Blin <oblin@mandriva.com> 4.3.0-5mdv2010.1
+ Revision: 524998
- suggest theme and drakx-installer packages instead of requiring them,
  one may want to just use mkcd --addmd5, which does not need all this
  (for example for Mandriva One build with draklive)

* Mon Feb 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.3.0-4mdv2010.1
+ Revision: 502343
- Clean spec file
- Use %%setup -q
- Fix rpmlint's warning

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.3.0-3mdv2010.0
+ Revision: 426146
- rebuild

* Thu Apr 23 2009 Antoine Ginies <aginies@mandriva.com> 4.3.0-2mdv2009.1
+ Revision: 368933
- final release

* Thu Feb 26 2009 Antoine Ginies <aginies@mandriva.com> 4.3.0-1mdv2009.1
+ Revision: 345286
- link noarch's i586 rpm on media/main of the 64b release to optimize dual arch CD space

* Thu Feb 26 2009 Antoine Ginies <aginies@mandriva.com> 4.2.9-1mdv2009.1
+ Revision: 345212
- add dual arch support for isolinux.cfg

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 4.2.8-2mdv2009.0
+ Revision: 223289
- rebuild

* Fri Mar 28 2008 Antoine Ginies <aginies@mandriva.com> 4.2.8-1mdv2008.1
+ Revision: 190890
- remove old tarball
- add xml-info option

* Tue Mar 04 2008 Antoine Ginies <aginies@mandriva.com> 4.2.7-4mdv2008.1
+ Revision: 178771
- revert to 4.2.7 version to be able to submit the package
- new tarball
- increase version

* Fri Feb 29 2008 Antoine Ginies <aginies@mandriva.com> 4.2.7-3mdv2008.1
+ Revision: 176797
- quick fix to avoid a big problem of rejected package because of missing suggests's dependencies

* Wed Feb 27 2008 Antoine Ginies <aginies@mandriva.com> 4.2.7-2mdv2008.1
+ Revision: 175786
- add nosuggests option

* Thu Feb 14 2008 Antoine Ginies <aginies@mandriva.com> 4.2.7-1mdv2008.1
+ Revision: 168240
- add some requires, add docbook documentation, add rpm's suggest support
- new release

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Added requires to packdrake.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4.2.6-1mdv2008.1
+ Revision: 130016
- kill re-definition of %%buildroot on Pixel's request
- fix URL


* Sat Mar 17 2007 Olivier Blin <oblin@mandriva.com> 4.2.6-1mdv2007.1
+ Revision: 145388
- 4.2.6
- make clean-rpmsrate handle LIVE flag in the same special way as INSTALL
- use /usr/share/bootsplash/scripts/make-boot-splash-raw to set the bootsplash inside all.rdz (warly)
- fix rpmsrate kernel regexp; make keys parsing in config file stricter (warly)
- bump to 4.2.6; print version when starting (warly)
- remove onlyifneeded flag for packages added to resolve deps of packages which are not needed but potentially included (warly)
- Import mkcd

* Tue Sep 26 2006 Warly <warly@mandriva.com> 4.2.5-1mdv2007.0
- Have a finer list space mechanism to include needed packages

* Sat Sep 23 2006 Warly <warly@mandriva.com> 4.2.4-1mdv2007.0
- Fix a bad calculation in available space on CDs during the build

* Fri Sep 22 2006 Warly <warly@mandriva.com> 4.2.3-1mdv2007.0
- 2007.0, handle dual arch mode

* Sat Apr 15 2006 Warly <warly@mandriva.com> 4.1.10-1mdk
- Automatically add pubkey when found in new --fixed hdlists mode

* Sat Apr 15 2006 Warly <warly@mandriva.com> 4.1.9-1mdk
- Fix --fixed hdlist regexp to correctly takes hdlist name and pubkey
- Add a new --hdlists:/path_to_hdlists to automatically include all the hdlist files of 
  a previous build set of CDs
- Fix checkDiscs functions in update mode not to stop if duplicate packages are found
- Update to packdrake-ng

* Tue Oct 18 2005 Warly <warly@mandriva.com> 4.1.8-1mdk
- fix automode

* Wed Sep 21 2005 Warly <warly@mandriva.com> 4.1.7-1mdk
- add explicit -udf option for boot

* Tue Sep 20 2005 Warly <warly@mandriva.com> 4.1.6-1mdk
- fix rpmsrate completion for packages like lib64kdenetwork2-kopete-devel

* Wed Aug 31 2005 Warly <warly@mandriva.com> 4.1.5-1mdk
- Correctly reject packages with their respective list
- Do not try to optimize space if the space is spread over too many CDs

* Thu Aug 04 2005 Warly <warly@mandriva.com> 4.1.4-1mdk
- Generate .idx packages list with each main ISO
- Add variable support in config file
- Rename default distro name to Mandriva 
- Do not go through calc_needed_size until a non-fixed rep is found

* Thu Apr 14 2005 Warly <warly@mandrakesoft.com> 4.1.3-1mdk
- Fix stupid syntax error

* Tue Apr 12 2005 Warly <warly@mandrakesoft.com> 4.1.2-1mdk
- Fix 'notinrep' and 'inrep' option not working properly

* Wed Mar 23 2005 Warly <warly@mandrakesoft.com> 4.1.1-1mdk
- add -udf for Xbox install
- take into account rpm version and release when creating the rpm list
  and checking for alternatives
- Fix a bad bug in dependencies checking for already done media

* Tue Mar 15 2005 Warly <warly@mandrakesoft.com> 4.1.0-1mdk
- first basic implementation of mkcd shell called with --shell
- fix checkdeps functions

* Tue Feb 22 2005 Warly <warly@mandrakesoft.com> 4.0.12-1mdk
- include size into the hdlists
- generate a media.cfg in media_info

* Fri Feb 04 2005 Warly <warly@mandrakesoft.com> 4.0.11-1mdk
- add mkcd.cgi for first test of a http frontend

* Wed Nov 03 2004 Warly <warly@mandrakesoft.com> 4.0.10-1mdk
- fix a option name overlapping (source) for 'fixed' and 'cdcom' command
- fix a bug to check duplicate packages (with same name and different versions)

* Sat Oct 09 2004 Warly <warly@mandrakesoft.com> 4.0.9-1mdk
- fix bad initialization of 'fixed' command associated list

* Tue Oct 05 2004 Warly <warly@mandrakesoft.com> 4.0.8-1mdk
- fix auto mode for 1st disc building
- fix cleanrpmsrate for slmodem and dkms_like packages
- fix a bug which make some package wrongly included in other list

* Thu Sep 16 2004 Warly <warly@mandrakesoft.com> 4.0.7-1mdk
- fix group conflict matrix initialized with wrong index
- fix limit option which was resetted when adding dependencies
- now 10.0 has no more a special way of dealing with extra CDs
- fix needed option sometimes increased in closeRpmsList making
  packages put on further CDs

* Wed Sep 15 2004 Warly <warly@mandrakesoft.com> 4.0.6-1mdk
- fix various important bugs
  * do not split one group over several IO-group
  * correctly create IO group list
- add a new "group" option to generic to force alone groups
  to be grouped in a certain way.

* Sat Sep 11 2004 Warly <warly@mandrakesoft.com> 4.0.5-1mdk
- fix (again) cd 1 creation in auto mode
- fix non selected alternatives that was sometimes used to solve a deps (now they are only used if no other deps exist)
- add new dkms-like package in clean-rpmsrate

* Sat Sep 04 2004 Warly <warly@mandrakesoft.com> 4.0.4-1mdk
- new inrep and notinrep filter list keywords
- better output for packages list 
- 'limit' is not taken as 'noalernatives' in filterlist
- new --ask_media option to installation to activate the media choice during installation

* Tue Aug 24 2004 Warly <warly@mandrakesoft.com> 4.0.3-1mdk
- fix a bug in auto mode using deprecated isolinux function

* Tue Aug 10 2004 Warly <warly@mandrakesoft.com> 4.0.2-1mdk
- die in cleanrpmsrate if duplicate are found
- new suppl_cd mode to create supplementary discs
- add DiscX extension in auto-mode to comply with stage one installation
  from ISO files on disk.
- use compssUsers.pl for structure 10.1

* Fri Jul 30 2004 Warly <warly@mandrakesoft.com> 4.0.1-1mdk
- fix a nasty bug in choosing alternative code which did 
  not reject packages when all the alternatives for a given 
  dependency are rejected (and which make the needed packages
  size calculation not correctly done, and result in more often 
  than normal "Could not fit on disc" dies)
- fix auto mode
- add new test_list mode to test file list inside configuration file

* Tue Jul 27 2004 Warly <warly@mandrakesoft.com> 4.0.0-1mdk
- extract the path structure info to make it configurable 
  (and switch between old and new structure)

* Sat Jul 24 2004 Warly <warly@mandrakesoft.com> 3.9.2-1mdk
- add new suppl option

* Tue Jul 06 2004 Warly <warly@mandrakesoft.com> 3.9.1-1mdk
- add a new fixed function to replace old cdcom command and have an easier
  interface
- fix a potential bug in multi-list dependencies checking for alternatives
  which may have rejected packages without reason.
- fix a dependencies checking problem when severa discs are build based on the
  same packages list

* Thu Jun 03 2004 Warly <warly@mandrakesoft.com> 3.9.0-1mdk
- Create a new subgroup with groups sharing common CDs (to be able to
  separate ISO files build and rpm lists build).
- Fix a bug in checking that scheduled packages on one particular CDs, 
  alongside with their dependencies, are still fitting and that the 
  given discs layout is correct.

* Tue Mar 30 2004 Warly <warly@mandrakesoft.com> 3.8.7-1mdk
- fix a deps ordering problem.

* Fri Mar 26 2004 Warly <warly@mandrakesoft.com> 3.8.6-1mdk
- fix kernel-\d+\.\d+ parsing

* Thu Mar 18 2004 Warly <warly@mandrakesoft.com> 3.8.5-1mdk
- add kernel-\d+\.\d+ support in rpmsrate (for eagle drivers)

