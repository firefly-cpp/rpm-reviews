%bcond_without tests

%global pypi_name matplotlib-venn

%global _description %{expand:
Venn diagram plotting routines for Python/Matplotlib. The package
provides four main functions: venn2, venn2_circles, venn3 and
venn3_circles.}


Name:           python-%{pypi_name}
Version:        0.11.7
Release:        1%{?dist}
Summary:        Routines for plotting area-weighted two- and three-circle venn diagrams.

License:        MIT
URL:            https://github.com/konstantint/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files matplotlib_venn

%check
%if %{with tests}
%pytest
%endif

%files -n python3-matplotlib-venn -f %{pyproject_files}
%license LICENSE
%doc README.rst DEVELOPER-README.rst CHANGELOG.txt

%changelog
* Wed Apr 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.11.7-1
- Initial package
