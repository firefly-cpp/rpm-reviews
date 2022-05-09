%bcond_without tests

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global pypi_name niaarm
%global pretty_name NiaARM

%global _description %{expand:
NiaARM is a framework for Association Rule Mining based on nature-inspired
algorithms for optimization. The framework is written fully in Python and
runs on all platforms. NiaARM allows users to preprocess the data in a
transaction database automatically, to search for association rules and
provide a pretty output of the rules found. This framework also supports
numerical and real-valued types of attributes besides the categorical ones.
Mining the association rules is defined as an optimization problem, and
solved using the nature-inspired algorithms that come from the related
framework called NiaPy.}

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        1%{?dist}
Summary:        A minimalistic framework for numerical association rule mining

License:        MIT

URL:            https://github.com/firefly-cpp/%{pretty_name}
Source0:        %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires %{?with_doc_pdf:-x docs}

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaarm

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/%{pypi_name}
%license LICENSE
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/
%doc paper/
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md

%changelog
* Sun May 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.6-1
- Upgrade to 0.1.6

* Sun Apr 10 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-1
- Initial package
