%define		_class		File
%define		_subclass	HtAccess
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate .htaccess files
Summary(pl.UTF-8):	%{_pearname} - manipulacje na plikach .htaccess
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	12cb3e3dbf284f9ffc5eca48a0a88bb5
URL:		http://pear.php.net/package/File_HtAccess/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-File_HtAccess-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods to manipulate .htaccess files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza metody do manipulowania plikami .htaccess.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
