%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Vector
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Vector and vector operation classes
Summary(pl):	%{_class}_%{_subclass} - Wektory i klasy operuj±ce na wektorach
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to represent Tuples, general Vectors, and 2D-/3D-vectors, as
well as a static class for vector operations.

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
