%global debug_package %{nil}
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global package_name rhos-bootstrap
%global py_name rhos_bootstrap

Name:           %{package_name}
Summary:        Red Hat OpenStack bootstrap utility
Version:        XXX
Release:        XXX

Group:          System Environment/Base
License:        ASL 2.0

URL:            https://github.com/redhat-openstack/rhos-bootstrap
Source:         https://github.com/redhat-openstack/rhos-bootstrap/archive/%{upstream_version}.tar.gz#/rhos-bootstrap-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3dist(setuptools)

Requires:       python3-libdnf
Requires:       python3-dnf
Requires:       python3-pyyaml
Requires:       python3-requests

Suggests:       subscription-manager

%{?python_provide:%python_provide python3-%{name}}

%description
A bootstrap tool used to handle repository, dnf module configuration, and
tripleoclient installation in preparation for a Red Hat OpenStack installation.

%prep
%autosetup -n %{package_name}-%{upstream_version} -S git
rm -rf *.egg-info

%build
%{py3_build}

%install
%{py3_install}
mv %{buildroot}/%{_datadir}/%{py_name} %{buildroot}/%{_datadir}/%{package_name}

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{py_name}*
%{_bindir}/%{package_name}
%{_datadir}/%{package_name}

%changelog
