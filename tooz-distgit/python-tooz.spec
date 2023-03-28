# Created by pyp2rpm-1.0.1
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global pypi_name tooz
%global with_doc 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
The Tooz project aims at centralizing the most common distributed primitives \
like group membership protocol, lock service and leader election by providing \
a coordination API helping developers to build distributed applications.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Coordination library for distributed systems

License:        ASL 2.0
URL:            https://tooz.readthedocs.org
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
BuildRequires:  openstack-macros
%endif

BuildRequires:  git-core

%description
%{common_desc}

%package -n     python3-%{pypi_name}
Summary:        Coordination library for distributed systems
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 2.0.0
Requires:       python3-fasteners
Requires:       python3-futurist
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-utils >= 4.7.0
Requires:       python3-pbr >= 1.6
Requires:       python3-stevedore >= 1.16.0
Requires:       python3-tenacity >= 5.0.0
Requires:       python3-voluptuous >= 0.8.9
Requires:       python3-zake
Requires:       python3-msgpack >= 0.4.0


Requires:       python3-redis

%description -n python3-%{pypi_name}
%{common_desc}

%if %{?with_doc}
%package doc
Summary:    Documentation for %{name}
Group:      Documentation
License:    ASL 2.0

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-fasteners
BuildRequires:  python3-futurist
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-stevedore >= 1.5.0
BuildRequires:  python3-sysv_ipc
BuildRequires:  python3-tenacity
BuildRequires:  python3-voluptuous
BuildRequires:  python3-pymemcache
BuildRequires:  python3-PyMySQL
BuildRequires:  python3-zake
BuildRequires:  python3-msgpack >= 0.4.0


BuildRequires:  python3-psycopg2
BuildRequires:  python3-redis

%description doc
%{common_desc}

This package contains documentation in HTML format.
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the requirements
rm -f {test-,}requirements.txt

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%{py3_build}

%if %{?with_doc}
# generate html docs
%{__python3} setup.py build_sphinx -b html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif


%install
%{py3_install}
rm -fr %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info

%if %{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
