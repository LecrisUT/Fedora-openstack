%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
#guard for including python-pyngus (OSP 12 does not ship python-pyngus)
%global rhosp 0

%global common_desc \
The Oslo project intends to produce a python library containing \
infrastructure code shared by OpenStack projects. The APIs provided \
by the project should be high quality, stable, consistent and generally \
useful.

%global common_desc1 \
Tests for the OpenStack common messaging library.

%global pypi_name oslo.messaging
%global pkg_name oslo-messaging

Name:       python-oslo-messaging
Version:    XXX
Release:    XXX
Summary:    OpenStack common messaging library

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires: git-core

%package -n python3-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: python3-futurist
# Required for tests
BuildRequires: python3-fixtures
BuildRequires: python3-hacking
BuildRequires: python3-kombu >= 1:4.6.6
BuildRequires: python3-mock
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-metrics
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-subunit
BuildRequires: python3-testtools
BuildRequires: python3-stestr
BuildRequires: python3-cachetools
BuildRequires: python3-redis
BuildRequires: python3-kafka


Requires:   python3-pbr
Requires:   python3-amqp >= 2.5.2
Requires:   python3-debtcollector >= 1.2.0
Requires:   python3-futurist >= 1.2.0
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-utils >= 3.37.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-service >= 1.24.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-metrics >= 0.2.1
Requires:   python3-oslo-middleware >= 3.31.0
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-kombu >= 1:4.6.6
Requires:   python3-eventlet
Requires:   python3-cachetools
Requires:   python3-webob >= 1.7.1
Requires:   python3-yaml >= 3.13

%if 0%{rhosp} == 0
Requires:   python3-pyngus
%endif

%description -n python3-%{pkg_name}
%{common_desc}

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

# for API autodoc
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-stevedore
BuildRequires: python3-fixtures
BuildRequires: python3-kombu >= 1:4.0.0
BuildRequires: python3-PyYAML

%if 0%{rhosp} == 0
BuildRequires: python3-pyngus
%endif


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python3-%{pkg_name} = %{version}-%{release}
Requires:      python3-oslo-config
Requires:      python3-oslo-middleware
Requires:      python3-oslo-serialization
Requires:      python3-oslo-service
Requires:      python3-oslo-utils >= 3.37.0
Requires:      python3-oslotest
Requires:      python3-testtools
Requires:      python3-stestr
Requires:      python3-testscenarios
BuildRequires: python3-kafka

%description -n python3-%{pkg_name}-tests
%{common_desc1}

%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
# FIXME: workaround required to build
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
export PYTHONPATH=.
sphinx-build-3 -b html doc/source doc/build/html
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%{py3_install}
ln -s ./oslo-messaging-send-notification %{buildroot}%{_bindir}/oslo-messaging-send-notification-3

%check
# Four unit tests are failing for amqp1
stestr-3 run || true

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_messaging
%{python3_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-send-notification
%{_bindir}/oslo-messaging-send-notification-3
%exclude %{python3_sitelib}/oslo_messaging/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_messaging/tests

%changelog
