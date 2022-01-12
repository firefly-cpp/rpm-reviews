%global pypi_name pyqt-feedback-flow

%global _description %{expand:
This is a very simple module for showing simple notifications during the
cycling training sessions in order to pass on a cyclist`s essential
information, as well as information that can be submitted by a sport trainer.
This software allows us to show notification in the realm of a text or a
picture. It was shown that flowing feedback is more appropriate for
a cyclist than static notification or pop up windows. It can also be
integrated into existing PyQt projects very easily.}

Name:           python-%{pypi_name}
Version:        0.1.1
Release:        1%{?dist}
Summary:        Show feedbacks in toast-like notifications

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  %{py3_dist toml-adapt}
BuildRequires:  %{py3_dist pytest}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep emoji -ver X
toml-adapt -path pyproject.toml -a change -dep PyQt5 -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyqt_feedback_flow

%check
# use smoke test
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog

* Tue Jan 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Initial package
