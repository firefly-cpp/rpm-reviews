%global pypi_name marshmallow

# generating docs disabled for now -- no makefile
%bcond_with doc_pdf
%bcond_without tests

%global _description %{expand:
marshmallow is an ORM/ODM/framework-agnostic library
for converting complex datatypes, such as objects,
to and from native Python datatypes.}

Name:           python-%{pypi_name}
Version:        3.15.0
Release:        1%{?dist}
Summary:        A library for converting complex objects to and from simple Python datatypes

License:        MIT
URL:            https://github.com/marshmallow-code/marshmallow
Source0:        %{pypi_source marshmallow}
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(simplejson)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

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
%autosetup -n marshmallow-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs/ latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files marshmallow

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE NOTICE
%doc README.rst

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif

%changelog
* Sun May 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 3.15.0-1
- Initial package
