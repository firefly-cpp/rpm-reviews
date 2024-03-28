%bcond_without check

%global packname niarules
%global rlibdir  %{_datadir}/R/library
%global ver 0.1.0

Name:             R-%{packname}
Version:          %{ver}
Release:          1%{?dist}
License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source:           %{url}&version=%{version}#/%{packname}_%{ver}.tar.gz
Summary:          Numerical Association Rule Mining using Nature-Inspired Algorithms

BuildRequires:    R-devel, tex(latex)

%if %{with check}
BuildRequires:    R-testthat
%endif

BuildArch:        noarch

%description
Framework is devoted to mining numerical association rules
through the utilization of nature-inspired algorithms for
optimization.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%doc %{rlibdir}/%{packname}/CONTRIBUTING.md
%doc %{rlibdir}/%{packname}/examples/
%doc %{rlibdir}/%{packname}/extdata/

%changelog
* Thu Mar 28 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
