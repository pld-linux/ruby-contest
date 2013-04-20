%define pkgname contest
Summary:	Write more readable tests in Test::Unit with this tiny script
Name:		ruby-%{pkgname}
Version:	0.1.3
Release:	1
License:	Distributable
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	3cdd786cfb051e176855eee40679968a
URL:		http://github.com/citrusbyte/contest
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Write declarative tests using nested contexts without performance
penalties. Contest is less than 100 lines of code and gets the job
done.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown LICENSE
%{ruby_vendorlibdir}/contest.rb
