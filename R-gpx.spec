%bcond_without check

%global packname gpx
%global ver 1.1.0

%global _description %{expand:
Process open standard GPX files into data.frames
for further use and analysis in R.}

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

%description %_description

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL -l %{buildroot}%{_datadir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check --ignore-vignettes %{packname}
%endif

%files
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/NEWS.md
%license %{_datadir}/R/library/%{packname}/LICENSE
%{_datadir}/R/library/%{packname}/DESCRIPTION
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help

%changelog
* Fri Mar 17 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.1.0-1
- Initial package
