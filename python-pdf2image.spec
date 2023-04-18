# do not test for now | missing dependency that is no longer maintained
# https://github.com/pythonprofilers/memory_profiler
%bcond_with tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We would like to generate PDF documentation as a substitute, but have not
# been able to successfully build the Sphinx-generated LaTeX for this
# particular package.

%bcond_without doc_pdf

%global forgeurl https://github.com/Belval/pdf2image
%global tag v.%{version}

Name:           python-pdf2image
Version:        1.16.3
%forgemeta
Release:        1%{?dist}
Summary:        Convert PDF to PIL Image object

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%global _description %{expand:
A wrapper around the pdftoppm and pdftocairo
command line tools to convert PDF to a PIL
Image list.}

%description %_description

%package -n python3-pdf2image
Summary:        %{summary}
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest) >= 3.7.1
BuildRequires:  poppler
%endif

%description -n python3-pdf2image %_description

%package doc
Summary:        Documentation and examples for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python-sphinx-latex
BuildRequires:  python3dist(recommonmark)
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
%endif

Requires:  poppler

%description doc
%{summary}.

Full HTML documentation is available at
https://belval.github.io/pdf2image/

%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet -f'
%endif

%install
%pyproject_install
%pyproject_save_files pdf2image

%check
%if %{with tests}
%pytest
%endif

%files -n python3-pdf2image -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/pdf2image.pdf
%endif

%changelog
* Mon Apr 17 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.16.3-1
- Initial package
