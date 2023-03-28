%global debug_package %{nil}
%{?!released_version: %global released_version 0.2.1}
%{?upstream_version: %global task_core_version git%{upstream_version}}
%{!?upstream_version: %global task_core_version %%{released_version}%{?milestone}}

Name:           task-core
Summary:        Python library for describing and resolving service dependencies
Version:        XXX
Release:        XXX

License:        ASL 2.0

URL:            https://github.com/Directord/task-core
Source0:        https://github.com/directord/%{name}/archive/%{task_core_version}.tar.gz#/%{name}-%{task_core_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0

%description
Python library for describing and resolving service dependencies

%package -n python3-%{name}
Summary:        Python library code for task-core

# python requirements
Requires:       python3-jsonschema
Requires:       python3-networkx
Requires:       python3-stevedore
Requires:       python3-taskflow
Requires:       python3-yaml
# these are backends
Recommends:     directord
Recommends:     python3-ansible-runner

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python library for describing and resolving service dependencies

%package -n %{name}-examples
Summary:        Example services and tasks for task-core

Requires:       python3-%{name}

%description -n %{name}-examples
Example service and tasks for task-core

%prep
%autosetup -n %{name}-%{upstream_version} -S git
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
# TODO(mwhahaha): run tests

%files -n python3-%{name}
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python3_sitelib}/task_core*
%exclude %{_datadir}/%{name}/examples

%files -n %{name}-examples
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{_bindir}/task-core-example
%{_datadir}/%{name}/examples

%changelog
