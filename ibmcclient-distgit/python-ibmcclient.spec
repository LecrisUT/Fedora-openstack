%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


%global library ibmcclient
%global _description \
python-ibmcclient is a Python library to communicate with HUAWEI `iBMC`\
based systems.\
\
The goal of the library is to be extremely simple, small, have as few\
dependencies as possible and be very conservative when dealing with BMCs\
by access HTTP REST API provided by HUAWEI `iBMC` based systems.\
\
Currently, the scope of the library has been limited to supporting\
OpenStack Ironic ibmc driver.\


Name:       python-%{library}
Version:    XXX
Release:    XXX
Summary:    Python library for managing HUAWEI iBMC based servers
License:    ASL 2.0
URL:        https://github.com/IamFive/python-ibmcclient

Source0:    https://github.com/IamFive/python-ibmcclient/archive/%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires: git-core

%description %{_description}


%package -n python3-%{library}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{library}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Unittest requirements
BuildRequires:  python3-requests
BuildRequires:  python3-mock
BuildRequires:  python3-responses

Requires:       python3-requests
Requires:       python3-six

%description -n python3-%{library} %{_description}


%prep
%autosetup -n %{name}-%{upstream_version} -S git

# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install


# the tests folder is excluded in manifest.in,
# so, no tests will be run here.
# %check
# %{__python3} setup.py test

%files -n python3-%{library}
%license LICENSE.txt
%doc README.rst CHANGELOG.md
%{python3_sitelib}/ibmc_client
%{python3_sitelib}/python_%{library}-*.egg-info
# %exclude %{python3_sitelib}/tests

%changelog
