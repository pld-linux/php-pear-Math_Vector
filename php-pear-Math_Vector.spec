%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Vector
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - vector and vector operation classes
Summary(pl):	%{_class}_%{_subclass} - wektory i klasy operuj±ce na wektorach
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c1c70ace9f00bf96142f717c42988657
URL:		http://pear.php.net/package/Math_Vector/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to represent Tuples, general Vectors, and 2D-/3D-vectors, as
well as a static class for vector operations.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasy do reprezentowania krotek, ogólnych wektorów oraz wektorów
2D/3D, a tak¿e statyczna klasa do operacji na wektorach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
