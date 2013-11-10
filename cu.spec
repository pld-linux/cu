Summary:	Simple unit testing framework for handling automated tests in C
Summary(pl.UTF-8):	Szkielet automatycznych testów jednostkowych dla języka C
Name:		cu
Version:	0.14.2
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://cu.danfis.cz/files/%{name}-%{version}.tar.gz
# Source0-md5:	fec662045ff1fd1d353fa93865abc80c
URL:		http://cu.danfis.cz/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
