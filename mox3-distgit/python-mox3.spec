# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Mox3 is a mock object framework for Python 3 and 2.7. \
Mox3 is an unofficial port of the Google mox framework to Python 3. It was \
meant to be as compatible with mox as possible, but small enhancements have \
been made.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/mox3
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:  python3-pbr
Requires:  python3-fixtures
Requires:  python3-six >= 1.9.0
Requires:  python3-testtools

BuildRequires:  python3-devel
BuildRequires:  python3-pbr

# test requires
BuildRequires:  python3-fixtures
BuildRequires:  python3-stestr
BuildRequires:  python3-subunit
BuildRequires:  python3-testtools
BuildRequires:  python3-six >= 1.9.0

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
%py_req_cleanup

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%check
PYTHON=python3 stestr-3 run

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info

%changelog
