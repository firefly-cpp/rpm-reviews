%bcond_without check

%global packname gpx
%global rlibdir  %{_libdir}/R/library
%global ver 1.1.0

Name:             R-%{packname}
Version:          %{ver}
Release:          1%{?dist}
Source0:          ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
License:          MIT
URL:              https://cran.r-project.org/web/packages/gpx/index.html
Summary:          Process GPX files

BuildRequires:    R-devel, tex(latex), R-xml2, R-lubridate, R-rvest
Requires:         R-core

%if %{with check}
BuildRequires:    R-testthat
%endif

BuildArch:        noarch

%description
Process open standard GPX files into data.frames
for further use and analysis in R. Github repository:
https://github.com/bmewing/gpx

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help

%changelog
* Fri Mar 17 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
