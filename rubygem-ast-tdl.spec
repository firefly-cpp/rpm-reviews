%global gem_name ast-tdl

%global _description %{expand:
ast-dsl is a small DSL for practical definition and
description of sports training that can be automatically or manually
defined and used in conjunction with Artificial Sport Trainer.}

Name: rubygem-%{gem_name}
Version: 0.0.2
Release: 1%{?dist}
Summary: An experimental and minimalistic Training Description Language
License: MIT
URL: https://github.com/firefly-cpp/ast-tdl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.0
BuildArch: noarch

# ast-tdl is used conjointly with ast-monitor
Recommends: %{py3_dist ast-monitor}

%description %_description

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# upstream provides no tests for now
%check
pushd .%{gem_instdir}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jun 15 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.2-1
- Initial package
