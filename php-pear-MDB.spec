%define		_class		MDB
%define		_pearname	%{_class}
%define		_status		stable

%define		_requires_exceptions pear(test_setup.php)\\|pear(PHPUnit.php)

Summary:	%{_pearname} - unified database API
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	%mkrel 10
Epoch:		1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/MDB/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{,Modules/{,Manager}}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/
install %{_pearname}-%{version}/%{_class}/*.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/%{_class}/Modules/*.php %{buildroot}%{_datadir}/pear/%{_class}/Modules/
install %{_pearname}-%{version}/%{_class}/Modules/Manager/*.php %{buildroot}%{_datadir}/pear/%{_class}/Modules/Manager/

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_datadir}/pear/%{_class}
%dir %{_datadir}/pear/%{_class}/Modules
%dir %{_datadir}/pear/%{_class}/Modules/Manager
%doc %{_pearname}-%{version}/{MAINTAINERS,README,TODO,doc/,tests/}
%{_datadir}/pear/*.php
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/Modules/*.php
%{_datadir}/pear/%{_class}/Modules/Manager/*.php
%{_datadir}/pear/packages/%{_pearname}.xml
