Summary:	Simple unit testing framework for handling automated tests in C
Summary(pl.UTF-8):	Szkielet automatycznych testów jednostkowych dla języka C
Name:		cu
Version:	0.15.1
Release:	3
License:	BSD
Group:		Development/Libraries
#Source0Download: https://github.com/danfis/cu/tags
Source0:	http://cu.danfis.cz/files/%{name}-%{version}.tar.gz
# Source0-md5:	bd5f70ea6f06e2a050c7e5e280043927
URL:		https://github.com/danfis/cu
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
CU is simple unit testing framework for handling automated tests in C.
CU provides a simple interface for defining unit tests using macros.
Each test suite runs in separate process - test suites don't influence
each other and any failure (such as segfault) does not break up whole
test. CU also provides script for regression tests based on output of
test suites.

%description -l pl.UTF-8
CU to prosty szkielet testów jednostkowych do obsługi
zautomatyzowanego testowania w języku C. Zapewnia prosty interfejs do
definiowania testów jednostkowych przy użyciu makr. Każdy zestaw
testów działa w osobnym procesie - zbiory testów nie przeszkadzają
sobie nawzajem i jedna awaria (taka jak segfault) nie psuje całości
testów. CU dostarcza także skrypt do testów regresji w oparciu o
wyjście zestawów testów.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' cu-check-regressions

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -pedantic"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	INCLUDEDIR=%{_includedir} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSD-LICENSE CHANGELOG
%attr(755,root,root) %{_bindir}/cu-check-regressions
%{_libdir}/libcu.a
%{_includedir}/cu.h
