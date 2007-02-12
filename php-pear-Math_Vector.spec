%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Vector
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - vector and vector operation classes
Summary(pl.UTF-8):   %{_class}_%{_subclass} - wektory i klasy operujące na wektorach
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c1c70ace9f00bf96142f717c42988657
URL:		http://pear.php.net/package/Math_Vector/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to represent Tuples, general Vectors, and 2D-/3D-vectors, as
well as a static class for vector operations.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy do reprezentowania krotek, ogólnych wektorów oraz wektorów
2D/3D, a także statyczna klasa do operacji na wektorach.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d docs/%{_pearname}/examples
mv ./%{php_pear_dir}/%{_class}/%{_subclass}/tests/examples/* docs/%{_pearname}/examples

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/%{_subclass}/tests/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
