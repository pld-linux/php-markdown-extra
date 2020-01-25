%define		php_min_version 5.0.0
Summary:	PHP Markdown with extra features
Name:		php-markdown-extra
Version:	1.2.5
Release:	1
License:	BSD-Style License
Group:		Development/Languages/PHP
Source0:	http://littoral.michelf.ca/code/php-markdown/%{name}-%{version}.zip
# Source0-md5:	17ff4ac9ecfe3bf629b640885a7b9431
URL:		http://michelf.ca/projects/php-markdown/extra/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautopear	pear
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
PHP Markdown Extra is a special version of PHP Markdown implementing
some features currently not available with the plain Markdown syntax.
You can download PHP Markdown Extra from the PHP Markdown home page.

%prep
%setup -qc
mv "PHP Markdown Extra %{version}"/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p markdown.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.text
%{php_data_dir}/markdown.php
