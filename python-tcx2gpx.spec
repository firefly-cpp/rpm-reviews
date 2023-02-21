%bcond_without tests

%global pypi_name tcx2gpx
%global fullversion 0.1.4

%global _description %{expand:
This module converts the Garmin tcx GPS file format to the
more commonly used gpx file format. Both formats are a form
of XML but there are some fields in the former that are not
present in the later. It uses two packages to do the grunt
work tcxparser and gpxpy.}

Name:           python-%{pypi_name}
Version:        %{?fullversion}
Release:        1%{?dist}
Summary:        Convert Garmin TPX to GPX

License:        GPLv3
URL:            https://gitlab.com/nshephard/tcx2gpx
Source0:        %{pypi_source tcx2gpx}
BuildArch:      noarch
# remove linters and development dependencies
Patch:          0001-Remove-linters.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pypi_name} %_description

# subpackage for tests
%package -n python3-%{pypi_name}-tests

Summary:        Tests for python3-%{pypi_name}

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
rm -f %{buildroot}/tests
%pyproject_save_files %{pypi_name}

%check
%if %{with tests}
%pytest
%endif
# additional test
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n python3-%{pypi_name}-tests
%doc %{python3_sitelib}/tests/

%changelog
* Mon Feb 20 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Initial package
