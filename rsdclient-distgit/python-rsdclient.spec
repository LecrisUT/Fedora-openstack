%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global sname rsdclient
%global pyname python_rsdclient

Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        OpenStack client plugin for Rack Scale Design

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{name}
Source0:        http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n     python3-%{sname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest >= 1.10.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-testrepository >= 0.0.18
BuildRequires:  python3-testtools >= 1.4.0

Requires:       python3-six >= 1.10.0
Requires:       python3-osc-lib >= 1.7.0
Requires:       python3-pbr >= 2.0
Requires:       python3-rsd-lib >= 1.2.0
%description -n python3-%{sname}
This is a client for the RSD Pod Manager API, which is based on OpenStack
client framework. It provides a Python API (rsdclient/v1 module) and a RSD
specific plugin for OpenStack client (rsdclient/osc).

%package -n python3-%{sname}-tests
Summary: python-rsdclient tests
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
Tests for python-rsdclient

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: python-rsdclient documentation
BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme >= 1.11.0

%description -n python-%{sname}-doc
Documentation for python-rsdclient
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
%{__python3} setup.py build_sphinx
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/%{pyname}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{pyname}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{pyname}

%files -n python3-%{sname}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{pyname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
