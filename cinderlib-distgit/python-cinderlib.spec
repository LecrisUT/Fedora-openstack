%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

%global pypi_name cinderlib
%global __brp_mangle_shebangs_exclude_from ^%{python3_sitelib}/cinderlib/bin/venv-privsep-helper$
%global common_summary Python library for direct usage of Cinder drivers without the services
%global common_desc \
The Cinder Library, also known as cinderlib, is a Python library that leverages \
the Cinder project to provide an object oriented abstraction around Cinder's \
storage drivers to allow their usage directly without running any of the Cinder \
services or surrounding services, such as KeyStone, MySQL or RabbitMQ. \
\
The library is intended for developers who only need the basic CRUD \
functionality of the drivers and don't care for all the additional features \
Cinder provides such as quotas, replication, multi-tenancy, migrations, \
retyping, scheduling, backups, authorization, authentication, REST API, etc.

Name:           python-%{pypi_name}
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        %{common_summary}

License:        ASL 2.0
URL:            https://docs.openstack.org/cinderlib/latest/
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
%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        %{common_summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

Requires:       python3-pbr
Requires:       python3-cinder-common >= 21.0.0.0
Requires:       python3-os-brick >= 6.1.0
Requires:       sudo
Requires:       python3-importlib-metadata >= 1.7.0

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-cinder-common
BuildRequires:  python3-os-brick

# Required for unit tests
BuildRequires:    python3-ddt
BuildRequires:    python3-stestr
BuildRequires:    python3-oslotest

%description -n python3-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:        Documentation for cinderlib

BuildRequires:  graphviz
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-sphinxcontrib-rsvgconverter

%description doc
This package contains the documentation files for %{pypi_name}.

%{common_desc}
%endif

%package -n python3-%{pypi_name}-tests-unit
Summary:        Cinderlib unit tests

Requires:    python3-%{pypi_name}
Requires:    python3-ddt
Requires:    python3-os-testr
Requires:    python3-oslotest

%description -n python3-%{pypi_name}-tests-unit
This package contains the unit tests for %{pypi_name}.

%{common_desc}

%package -n python3-%{pypi_name}-tests-functional
Summary:        Cinderlib unit tests

Requires:    python3-%{pypi_name}
Requires:    python3-ddt
Requires:    python3-os-testr
Requires:    python3-oslotest

%description -n python3-%{pypi_name}-tests-functional
This package contains the functional tests for %{pypi_name}.

%{common_desc}

%package -n python3-%{pypi_name}-tests
Summary:        All cinderlib tests

Requires: python3-%{pypi_name}-tests-unit
Requires: python3-%{pypi_name}-tests-functional

%description -n python3-%{pypi_name}-tests
Virtual package for all %{pypi_name} tests.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove the requirements file so that pbr hooks don't add its requirements
rm -rf {test-,}requirements.txt

# Remove the devstack plugin, gate playbooks, and CI tools
rm -rf devstack playbooks tools

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/{.doctrees,.buildinfo,.placeholder,_sources}
%endif

%check
# (TODO) current master branch is for Yoga development and not compatible with
# cinder from zed. Ignoring unit tests errors until yoga version is released and
# master branch fixed
stestr run | true

%install
%{py3_install}

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/cinderlib*
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pypi_name}-tests-unit
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests/unit/*

%files -n python3-%{pypi_name}-tests-functional
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests/functional/*

%files -n python3-%{pypi_name}-tests
%exclude /*

%changelog
