%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1

%global common_desc \
Client library and command line utility for interacting with Openstack Designate API

%global sname designateclient

Name:       python-%{sname}
Version:    XXX
Release:    XXX
Summary:    Python API and CLI for OpenStack Designate

License:    ASL 2.0
URL:        https://launchpad.net/python-%{sname}/
Source0:    https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires: git-core
BuildRequires: openstack-macros

%description
%{common_desc}

%package -n python3-%{sname}
Summary:    Python API and CLI for OpenStack Designate
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Requires: python3-pbr >= 2.0.0
Requires: python3-keystoneauth1 >= 3.4.0
Requires: python3-requests >= 2.14.2
Requires: python3-stevedore >= 1.20.0
Requires: python3-osc-lib >= 1.8.0
Requires: python3-debtcollector >= 1.2.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-cliff >= 2.8.0
Requires: python3-jsonschema >= 3.2.0

%description -n python3-%{sname}
%{common_desc}


%package -n python3-%{sname}-tests
Summary:    Python API and CLI for OpenStack Designate (tests)
%{?python_provide:%python_provide python3-%{sname}-tests}
Requires:	python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
%{common_desc}

This package contains Designate client tests files.

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Designate API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-sphinxcontrib-apidoc
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-osc-lib
BuildRequires:    python3-jsonschema
BuildRequires:    python3-oslo-serialization

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
PYTHONPATH=. sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{sname}

%doc README.rst
%license LICENSE

%{python3_sitelib}/designateclient
%exclude %{python3_sitelib}/%{sname}/tests
%{python3_sitelib}/*.egg-info

%files -n python3-%{sname}-tests
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
