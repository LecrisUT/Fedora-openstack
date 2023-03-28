%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global service watcher
%global common_desc Watcher is an Infrastructure Optimization service.
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1

Name:           openstack-%{service}
Version:        XXX
Release:        XXX
Summary:        Openstack Infrastructure Optimization service.
License:        ASL 2.0
URL:            https://launchpad.net/watcher
Source0:        https://tarballs.openstack.org/%{service}/python-%{service}-%{upstream_version}.tar.gz

# Systemd scripts
Source10:       openstack-watcher-api.service
Source11:       openstack-watcher-applier.service
Source12:       openstack-watcher-decision-engine.service
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{service}/python-%{service}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-oslo-config >= 2:6.8.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 3.1.1
BuildRequires:  systemd
BuildRequires:  python3-debtcollector
BuildRequires:  python3-APScheduler
BuildRequires:  python3-microversion-parse


%description
%{common_desc}

%package -n     python3-%{service}
Summary:        Watcher Python libraries
%{?python_provide:%python_provide python3-%{service}}

Requires:       python3-APScheduler >= 3.5.1
Requires:       python3-croniter >= 0.3.20
Requires:       python3-os-resource-classes >= 0.4.0
Requires:       python3-jsonpatch >= 1.21
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-keystonemiddleware >= 4.21.0
Requires:       python3-oslo-concurrency >= 3.26.0
Requires:       python3-oslo-cache >= 1.29.0
Requires:       python3-oslo-config >= 2:6.8.0
Requires:       python3-oslo-context >= 2.21.0
Requires:       python3-oslo-db >= 4.44.0
Requires:       python3-oslo-i18n >= 3.20.0
Requires:       python3-oslo-log >= 3.37.0
Requires:       python3-oslo-messaging >= 14.1.0
Requires:       python3-oslo-policy >= 3.6.0
Requires:       python3-oslo-reports >= 1.27.0
Requires:       python3-oslo-serialization >= 2.25.0
Requires:       python3-oslo-service >= 1.30.0
Requires:       python3-oslo-upgradecheck >= 1.3.0
Requires:       python3-oslo-utils >= 3.36.0
Requires:       python3-oslo-versionedobjects >= 1.32.0
Requires:       python3-pbr >= 3.1.1
Requires:       python3-pecan >= 1.3.2
Requires:       python3-prettytable >= 0.7.2
Requires:       python3-cinderclient >= 3.5.0
Requires:       python3-glanceclient >= 1:2.9.1
Requires:       python3-gnocchiclient >= 7.0.1
Requires:       python3-ironicclient >= 2.5.0
Requires:       python3-keystoneclient >= 1:3.15.0
Requires:       python3-microversion-parse >= 0.2.1
Requires:       python3-monascaclient >= 1.12.0
Requires:       python3-neutronclient >= 6.7.0
Requires:       python3-novaclient >= 1:14.1.0
Requires:       python3-openstackclient >= 3.14.0
Requires:       python3-sqlalchemy >= 1.2.5
Requires:       python3-stevedore >= 1.28.0
Requires:       python3-taskflow >= 3.8.0
Requires:       python3-wsme >= 0.9.2
Requires:       python3-futurist >= 1.8.0

Requires:       python3-lxml >= 4.5.1
Requires:       python3-networkx >= 2.4
Requires:       python3-paste-deploy >= 1.5.2
Requires:       python3-webob >= 1.8.5

%description -n python3-%{service}
Watcher provides a flexible and scalable resource optimization service for
multi-tenant OpenStack-based clouds. Watcher provides a complete optimization
loop—including everything from a metrics receiver, complex event processor
and profiler, optimization processor and an action plan applier. This provides
a robust framework to realize a wide range of cloud optimization goals,
including the reduction of data center operating costs, increased system
performance via intelligent virtual machine migration, increased energy
efficiency—and more!

This package contains the Python libraries.

%package common

Summary: Components common for OpenStack Watcher

Requires: python3-%{service} = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description common
Watcher provides a flexible and scalable resource optimization service
for multi-tenant OpenStack-based clouds. Watcher provides a complete
optimization loop—including everything from a metrics receiver, complex
event processor and profiler, optimization processor and an action
plan applier. This provides a robust framework to realize a wide range of
cloud optimization goals, including the reduction of data center
operating costs, increased system performance via intelligent virtual
machine migration, increased energy efficiency—and more!

This package contains the common files.

%package api

Summary:     OpenStack Watcher API service
Requires:    %{name}-common = %{version}-%{release}

%description api
%{common_desc}

This package contains the ReST API.

%package applier
Summary:     OpenStack Watcher Applier service
Requires:    %{name}-common = %{version}-%{release}

%description applier
%{common_desc}

This package contains the watcher applier, which is one of core services of
watcher.

%package     decision-engine
Summary:     OpenStack Watcher Decision Engine service
Requires:    %{name}-common = %{version}-%{release}

%description decision-engine
%{common_desc}

This package contains the Watcher Decision Engine, which is one of core
services of watcher.

%package -n     python3-%{service}-tests-unit
Summary:        Watcher unit tests
%{?python_provide:%python_provide python3-%{service}-tests-unit}
Requires:       %{name}-common = %{version}-%{release}

%description -n python3-watcher-tests-unit
This package contains the Watcher test files.

%if 0%{?with_doc}
%package        doc
Summary:        Documentation for OpenStack Workflow Service

BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-db
BuildRequires:  python3-oslo-cache
BuildRequires:  python3-croniter
BuildRequires:  python3-jsonschema
BuildRequires:  python3-os-testr
BuildRequires:  python3-pecan
BuildRequires:  python3-subunit
BuildRequires:  python3-cinderclient
BuildRequires:  python3-glanceclient
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-novaclient
BuildRequires:  python3-monascaclient
BuildRequires:  python3-gnocchiclient
BuildRequires:  python3-keystonemiddleware
BuildRequires:  python3-ironicclient
BuildRequires:  python3-openstackclient
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-sphinxcontrib-pecanwsme
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-policy
BuildRequires:  python3-oslo-versionedobjects
BuildRequires:  python3-oslo-messaging
BuildRequires:  python3-oslo-reports
BuildRequires:  python3-reno
BuildRequires:  python3-jsonpatch
BuildRequires:  python3-taskflow
BuildRequires:  python3-wsme
BuildRequires:  python3-voluptuous
BuildRequires:  python3-debtcollector
BuildRequires:  openstack-macros

BuildRequires:  python3-freezegun
BuildRequires:  python3-networkx
BuildRequires:  python3-sphinxcontrib-httpdomain


%description    doc
OpenStack Watcher documentaion.

This package contains the documentation
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n python-%{service}-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}
oslo-config-generator --config-file etc/watcher/oslo-config-generator/watcher.conf  \
                      --output-file etc/watcher.conf.sample

%install
%{py3_install}

%if 0%{?with_doc}
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

mkdir -p %{buildroot}%{_sysconfdir}/watcher/
mkdir -p %{buildroot}%{_localstatedir}/log/watcher
mkdir -p %{buildroot}%{_localstatedir}/run/watcher
mkdir -p %{buildroot}%{_localstatedir}/cache/watcher

install -p -D -m 644 %SOURCE10 %{buildroot}%{_unitdir}/openstack-watcher-api.service
install -p -D -m 644 %SOURCE11 %{buildroot}%{_unitdir}/openstack-watcher-applier.service
install -p -D -m 644 %SOURCE12 %{buildroot}%{_unitdir}/openstack-watcher-decision-engine.service

install -p -D -m 640 etc/watcher.conf.sample \
                     %{buildroot}%{_sysconfdir}/watcher/watcher.conf
chmod +x %{buildroot}%{_bindir}/watcher*

# Remove unneeded in production
rm -f %{buildroot}/usr/etc/watcher.conf.sample
rm -f %{buildroot}/usr/etc/watcher/README-watcher.conf.txt
rm -rf %{buildroot}/usr/etc/watcher/oslo-config-generator

# Move /usr/etc/watcher to /etc/watcher
rm -rf %{buildroot}/usr/etc

%pre common
USERNAME=watcher
GROUPNAME=$USERNAME
HOMEDIR=%{_localstatedir}/cache/$USERNAME
getent group $GROUPNAME >/dev/null || groupadd -r $GROUPNAME
getent passwd $USERNAME >/dev/null ||
    useradd -r -g $GROUPNAME -G $GROUPNAME -d $HOMEDIR -s /sbin/nologin \
            -c "Satcher Services" $USERNAME
exit 0

%post api
%systemd_post openstack-watcher-api.service
%preun api
%systemd_preun openstack-watcher-api.service
%postun api
%systemd_postun_with_restart openstack-watcher-api.service

%post applier
%systemd_post openstack-watcher-applier.service
%preun applier
%systemd_preun openstack-watcher-applier.service
%postun applier
%systemd_postun_with_restart openstack-watcher-applier.service

%post decision-engine
%systemd_post openstack-watcher-decision-engine.service
%preun decision-engine
%systemd_preun openstack-watcher-decision-engine.service
%postun decision-engine
%systemd_postun_with_restart openstack-watcher-decision-engine.service

%files api
%license LICENSE
%{_bindir}/watcher-api
%{_bindir}/watcher-api-wsgi
%{_unitdir}/openstack-watcher-api.service

%files common
%license LICENSE
%dir %{_sysconfdir}/watcher
%config(noreplace) %attr(-, watcher, watcher) %{_sysconfdir}/watcher/*
%{_bindir}/watcher-db-manage
%dir %attr(755, watcher, watcher) %{_localstatedir}/run/watcher
%dir %attr(750, watcher, root) %{_localstatedir}/log/watcher
%dir %attr(755, watcher, watcher) %{_localstatedir}/cache/watcher
%{_bindir}/watcher-sync
%{_bindir}/watcher-status

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%files applier
%license LICENSE
%{_bindir}/watcher-applier
%{_unitdir}/openstack-watcher-applier.service

%files decision-engine
%license LICENSE
%{_bindir}/watcher-decision-engine
%{_unitdir}/openstack-watcher-decision-engine.service


%files -n python3-%{service}
%license LICENSE
%{python3_sitelib}/%{service}
%{python3_sitelib}/python_%{service}-*.egg-info
%exclude %{python3_sitelib}/%{service}/tests

%files -n python3-%{service}-tests-unit
%license LICENSE
%{python3_sitelib}/%{service}/tests

%changelog
