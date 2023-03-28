%{!?upstream_version: %global upstream_version %{version}}
%global pypi_name tcib

%global common_desc A repository to build OpenStack Services container \
images.

%{?!_licensedir:%global license %%doc}

Name:           python-%{pypi_name}
Summary:        A repository to build container images
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://github.com/openstack-k8s-operators/tcib
Source0:        https://pypi.io/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  git-core
BuildRequires:  python3-pbr
BuildRequires:  openstack-macros

# testing requirements
BuildRequires:  python3-stestr
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-requests-mock
BuildRequires:  python3-osc-lib
BuildRequires:  python3-tenacity
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-osc-lib-tests
BuildRequires:  python3-oslo-log
BuildRequires:  python3-ansible-runner

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:   A repository to build container images

Requires: python3-pbr >= 2.0.0
Requires: python3-openstackclient >= 5.2.0
Requires: (python3dist(ansible) >= 2.2 or ansible-core >= 2.11)
Requires: python3-ansible-runner >= 1.4.5
Requires: python3-osc-lib >= 2.3.0
Requires: python3-oslo-config >= 2:5.2.0
Requires: python3-oslo-log >= 3.36.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-concurrency >= 3.26.0
Requires: python3-tenacity >= 6.1.0
Requires: python3-requests >= 2.18.0
Requires: python3-yaml >= 3.12

Requires: %{name}-containers = %{version}-%{release}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%prep

%autosetup -n %{pypi_name}-%{upstream_version} -S git
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
export PYTHON=%{__python3}
stestr run

%package containers
Summary:   A repository to build container images

%description containers
This package installs the dependencies and files which are required on the base
TCIB container image.

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{_datadir}/ansible/roles/
# Exclude build_containers ci specific role
%exclude %{_datadir}/%{pypi_name}/container-images

%files containers
%{_datadir}/%{pypi_name}

%changelog

