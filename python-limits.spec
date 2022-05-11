%bcond_with tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
# It is disabled for now (problems with csv graphics)
%bcond_with doc_pdf

%global pypi_name limits

%global _description %{expand:
This package is a python library to perform rate
limiting with commonly used storage backends
(Redis, Memcached & MongoDB).}

Name:           python-%{pypi_name}
Version:        2.6.1
Release:        1%{?dist}
Summary:        Utilities to implement rate limiting using various strategies

License:        MIT
URL:            https://github.com/alisaifee/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist flaky}
BuildRequires:  %{py3_dist pytest-xdist}
BuildRequires:  %{py3_dist codecov}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytest-lazy-fixture}
BuildRequires:  %{py3_dist pytest-asyncio}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

# several dependencies are missing
# will be enabled later
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxext-opengraph}
BuildRequires:  %{py3_dist sphinx-copybutton}
BuildRequires:  %{py3_dist sphinx-autobuild}
BuildRequires:  %{py3_dist sphinx-panels}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files limits

# no tests in official GitHub release
# use smoke tests instead
%check
%if %{with tests}
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%files doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc doc/_build/latex/%{pypi_name}.pdf
%endif


%changelog
* Wed May 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.6.1-1
- Initial package
