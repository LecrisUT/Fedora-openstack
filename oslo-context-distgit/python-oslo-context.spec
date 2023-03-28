%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name oslo.context
%global pkg_name oslo-context
%global with_doc 1

%global common_desc \
The OpenStack Oslo context library has helpers to maintain \
useful information about a request context. \
The request context is usually populated in the \
WSGI pipeline and used by various modules such as logging.

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        OpenStack Oslo Context library

License:        ASL 2.0
URL:            https://launchpad.net/oslo.context
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%package -n python3-%{pkg_name}
Summary:        OpenStack Oslo Context library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# test dependencies
BuildRequires:  python3-debtcollector
BuildRequires:  python3-fixtures
BuildRequires:  python3-hacking
BuildRequires:  python3-oslotest

Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-pbr

%description -n python3-%{pkg_name}
%{common_desc}

%package -n python3-%{pkg_name}-tests
Summary:   Tests for OpenStack Oslo context library

Requires:  python3-%{pkg_name} = %{version}-%{release}

%description -n python3-%{pkg_name}-tests
Tests for OpenStack Oslo context library

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        Documentation for the OpenStack Oslo context library

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{pkg_name}-doc
Documentation for the OpenStack Oslo context library.
%endif

%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
# doc
sphinx-build-3 -b html doc/source doc/build/html
# Remove the sphinx-build-3 leftovers
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
python3 setup.py test

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_context
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_context/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pkg_name}-tests
%license LICENSE
%{python3_sitelib}/oslo_context/tests

%changelog
