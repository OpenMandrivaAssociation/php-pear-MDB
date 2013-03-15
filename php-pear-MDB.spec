%define		_class		MDB
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.3.0
Release:	20
Summary:	Unified database API
Epoch:		1
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/MDB/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/MAINTAINERS
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/TODO
%doc %{upstream_name}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-17mdv2011.0
+ Revision: 667557
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-16mdv2011.0
+ Revision: 607114
- rebuild

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.3.0-15mdv2010.1
+ Revision: 470164
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.3.0-14mdv2010.0
+ Revision: 426651
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-13mdv2009.1
+ Revision: 321871
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:1.3.0-12mdv2009.0
+ Revision: 224752
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-11mdv2008.1
+ Revision: 178522
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-10mdv2008.0
+ Revision: 53908
- the xml in package*.xml is valid now, don't reverse it...

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-9mdv2008.0
+ Revision: 15469
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-8mdv2007.0
+ Revision: 81172
- Import php-pear-MDB

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- initial Mandriva package (PLD import)

