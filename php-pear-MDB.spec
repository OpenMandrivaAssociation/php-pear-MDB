%define _class		MDB
%define modname	%{_class}

Summary:	Unified database API
Name:		php-pear-%{modname}
Epoch:		1
Version:	1.3.0
Release:	29
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/MDB/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
MDB is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/MAINTAINERS
%doc %{modname}-%{version}/README
%doc %{modname}-%{version}/TODO
%doc %{modname}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml

