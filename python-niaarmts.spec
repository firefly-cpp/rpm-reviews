%bcond_without tests

# we do not build docs since current docs are immature
%bcond_with doc_pdf

%global pypi_name NiaARMTS

%global _description %{expand:
framework is designed for numerical association rule mining in time series data using
stochastic population-based nature-inspired algorithms. It provides tools to extract
association rules from time series datasets while incorporating key metrics such as
support, confidence, inclusion, and amplitude. Although independent from the NiaARM
framework, this software can be viewed as an extension, with additional support
for time series numerical association rule mining. }

Name:           python-niaarmts
Version:        0.1.5
Release:        1%{?dist}
Summary:        Nature-Inspired Algorithms for Time Series Numerical Association Rule Mining

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3-toml-adapt
BuildRequires:  python3-pytest

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
%endif

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# relax pandas dependency versions
toml-adapt -path pyproject.toml -a change -dep pandas -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaarmts

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/niaarmts.pdf
%endif

%changelog
* Mon Apr 14 2025 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Initial package
