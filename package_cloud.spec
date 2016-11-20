#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	https://packagecloud.io
Name:		package_cloud
Version:	0.2.39
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	6af669feab1fab323b6b18d47e603cbb
URL:		https://packagecloud.io
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-rake
%endif
Requires:	ruby-highline = 1.6.20
Requires:	ruby-json_pure = 1.8.1
Requires:	ruby-rainbow = 2.1.0
Requires:	ruby-rest-client < 1.7
Requires:	ruby-rest-client >= 1.6.7
Requires:	ruby-thor < 1
Requires:	ruby-thor >= 0.18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
https://packagecloud.io.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/package_cloud
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{ruby_specdir}/%{name}-%{version}.gemspec
