%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Vector
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - vector and vector operation classes
Summary(pl.UTF-8):	%{_class}_%{_subclass} - wektory i klasy operujące na wektorach
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8a35077718ffa00e90b75bbd26419932
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

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/CompactedTuple.php
%{php_pear_dir}/Math/Tuple.php
%{php_pear_dir}/Math/Vector.php
%{php_pear_dir}/Math/Vector2.php
%{php_pear_dir}/Math/Vector3.php
%{php_pear_dir}/Math/VectorOp.php

%{_examplesdir}/%{name}-%{version}
