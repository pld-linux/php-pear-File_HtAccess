%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	HtAccess
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - manipulate .htaccess files
Summary(pl):	%{_pearname} - manipulacje na plikach .htaccess
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	d8db49e0b9d94f857f01977ef47c6ec8
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/File_HtAccess/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods to manipulate .htaccess files.

In PEAR status of this package is: %{_status}.

%description -l pl
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
