%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}
%global rhosp 0
%global service heat

%global common_desc \
Heat is a service to orchestrate composite cloud applications using a \
declarative template format through an OpenStack-native REST API.


Name:           openstack-%{service}
Summary:        OpenStack Orchestration (%{service})
# Liberty semver reset
# https://review.openstack.org/#/q/I6a35fa0dda798fad93b804d00a46af80f08d475c,n,z
Epoch:          1
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            http://www.openstack.org
Source0:        https://tarballs.openstack.org/%{service}/%{name}-%{upstream_version}.tar.gz
Obsoletes:      %{service} < 7-9
Provides:       %{service}

Source1:        %{service}.logrotate
Source2:        openstack-%{service}-api.service
Source3:        openstack-%{service}-api-cfn.service
Source4:        openstack-%{service}-engine.service
Source6:        openstack-%{service}-all.service

Source20:       %{service}-dist.conf
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{service}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires: git-core
BuildRequires: openstack-macros
BuildRequires: python3-devel
BuildRequires: python3-stevedore >= 1.20.0
BuildRequires: python3-oslo-cache
BuildRequires: python3-oslo-context
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-policy
BuildRequires: python3-oslo-messaging
BuildRequires: python3-setuptools
BuildRequires: python3-oslo-i18n
BuildRequires: python3-oslo-db
BuildRequires: python3-oslo-upgradecheck
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-log
BuildRequires: python3-oslo-versionedobjects
BuildRequires: python3-eventlet
BuildRequires: python3-kombu
BuildRequires: python3-netaddr
BuildRequires: python3-neutron-lib
BuildRequires: python3-osprofiler
BuildRequires: python3-six
BuildRequires: python3-paramiko
BuildRequires: python3-yaql
# These are required to build due to the requirements check added
BuildRequires: python3-routes
BuildRequires: python3-sqlalchemy
BuildRequires: python3-pbr
BuildRequires: python3-cryptography
# These are required to build the config file
BuildRequires: python3-oslo-config
BuildRequires: python3-keystoneauth1
BuildRequires: python3-keystoneclient
BuildRequires: python3-tenacity >= 4.4.0
# Required to compile translation files
BuildRequires: python3-babel

BuildRequires: python3-yaml
BuildRequires: python3-lxml
BuildRequires: python3-migrate
BuildRequires: python3-paste-deploy
BuildRequires: python3-redis
BuildRequires: python3-webob

BuildRequires: systemd

%if 0%{?with_doc}
BuildRequires: python3-openstackdocstheme
BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-cinderclient
BuildRequires: python3-novaclient
BuildRequires: python3-saharaclient
BuildRequires: python3-neutronclient
BuildRequires: python3-swiftclient
BuildRequires: python3-heatclient
BuildRequires: python3-glanceclient
BuildRequires: python3-troveclient
BuildRequires: python3-aodhclient
BuildRequires: python3-barbicanclient
BuildRequires: python3-designateclient
BuildRequires: python3-magnumclient
BuildRequires: python3-monascaclient
BuildRequires: python3-manilaclient
BuildRequires: python3-zaqarclient
BuildRequires: python3-croniter
BuildRequires: python3-gabbi
BuildRequires: python3-testscenarios
BuildRequires: python3-tempest
BuildRequires: python3-gabbi
# NOTE(ykarel) zunclient are not packaged yet.
#BuildRequires: python3-zunclient
%endif

Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: %{name}-engine = %{epoch}:%{version}-%{release}
Requires: %{name}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-api-cfn = %{epoch}:%{version}-%{release}

%package -n python3-%{service}-tests
%{?python_provide:%python_provide python3-%{service}-tests}
Summary:        Heat tests
Requires:       %{name}-common = %{epoch}:%{version}-%{release}

Requires: python3-oslotest
Requires: python3-testresources
Requires: python3-oslotest
Requires: python3-oslo-log >= 4.3.0
Requires: python3-oslo-utils >= 4.5.0
Requires: python3-heatclient
Requires: python3-cinderclient
Requires: python3-zaqarclient
Requires: python3-keystoneclient
Requires: python3-swiftclient
Requires: python3-paramiko
Requires: python3-kombu
Requires: python3-oslo-config >= 6.8.0
Requires: python3-oslo-concurrency
Requires: python3-requests >= 2.23.0
Requires: python3-eventlet >= 0.18.2
Requires: python3-gabbi
Requires: python3-ddt >= 1.4.1
Requires: python3-yaml >= 5.1

%description -n python3-%{service}-tests
%{common_desc}
This package contains the Heat test files.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n openstack-%{service}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

# Remove tests in contrib
find contrib -name tests -type d | xargs rm -r

%build
%{py3_build}

# Generate i18n files
%{__python3} setup.py compile_catalog -d build/lib/%{service}/locale

# Generate sample config and add the current directory to PYTHONPATH so
# oslo-config-generator doesn't skip heat's entry points.
PYTHONPATH=. oslo-config-generator --config-file=config-generator.conf

%install
%{py3_install}
sed -i -e '/^#!/,1 d' %{buildroot}/%{python3_sitelib}/%{service}/db/sqlalchemy/migrate_repo/manage.py

mkdir -p %{buildroot}/%{_localstatedir}/log/%{service}/
mkdir -p %{buildroot}/%{_localstatedir}/run/%{service}/
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-%{service}

# install systemd unit files
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/openstack-%{service}-api.service
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/openstack-%{service}-api-cfn.service
install -p -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/openstack-%{service}-engine.service
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/openstack-%{service}-all.service

mkdir -p %{buildroot}/%{_sharedstatedir}/%{service}/
mkdir -p %{buildroot}/%{_sysconfdir}/%{service}/

%if 0%{?with_doc}
sphinx-build -b html doc/source doc/build/html
sphinx-build -b man doc/source doc/build/man
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 doc/build/man/*.1 %{buildroot}%{_mandir}/man1/
%endif

rm -f %{buildroot}/%{_bindir}/%{service}-db-setup
rm -f %{buildroot}/%{_mandir}/man1/%{service}-db-setup.*
rm -rf %{buildroot}/var/lib/%{service}/.dummy
rm -f %{buildroot}/usr/bin/cinder-keystone-setup

install -p -D -m 640 etc/%{service}/%{service}.conf.sample %{buildroot}/%{_sysconfdir}/%{service}/%{service}.conf
install -p -D -m 640 %{SOURCE20} %{buildroot}%{_datadir}/%{service}/%{service}-dist.conf
echo '[revision]' >> %{buildroot}%{_datadir}/%{service}/%{service}-dist.conf
echo '%{service}_revision=%{version}' >> %{buildroot}%{_datadir}/%{service}/%{service}-dist.conf
mv %{buildroot}%{_prefix}/etc/%{service}/api-paste.ini %{buildroot}/%{_sysconfdir}/%{service}
mv %{buildroot}%{_prefix}/etc/%{service}/environment.d %{buildroot}/%{_sysconfdir}/%{service}
mv %{buildroot}%{_prefix}/etc/%{service}/templates %{buildroot}/%{_sysconfdir}/%{service}
# Remove duplicate config files under /usr/etc/heat
rmdir %{buildroot}%{_prefix}/etc/%{service}

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/%{service}/locale/*/LC_*/%{service}*po
rm -f %{buildroot}%{python3_sitelib}/%{service}/locale/*pot
mv %{buildroot}%{python3_sitelib}/%{service}/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang %{service} --all-name

%description
%{common_desc}

%package common
Summary: Heat common
Group: System Environment/Base

Obsoletes: %{name}-api-cloudwatch < %{epoch}:10.0.0

Requires: python3-pbr >= 3.1.1
Requires: python3-croniter >= 0.3.4
Requires: python3-eventlet >= 0.18.2
Requires: python3-stevedore >= 3.1.0
Requires: python3-netaddr >= 0.7.18
Requires: python3-neutron-lib >= 1.14.0
Requires: python3-osprofiler >= 1.4.0
Requires: python3-requests >= 2.23.0
Requires: python3-routes >= 2.3.1
Requires: python3-sqlalchemy >= 1.4.0
Requires: python3-paramiko
Requires: python3-babel >= 2.3.4
# FIXME: system version is stuck to 1.7.2 for cryptography
Requires: python3-cryptography >= 2.5
Requires: python3-yaql >= 1.1.3

Requires: python3-oslo-cache >= 1.26.0
Requires: python3-oslo-concurrency >= 3.26.0
Requires: python3-oslo-config >= 2:6.8.0
Requires: python3-oslo-context >= 2.22.0
Requires: python3-oslo-upgradecheck >= 1.3.0
Requires: python3-oslo-utils >= 4.5.0
Requires: python3-oslo-db >= 6.0.0
Requires: python3-oslo-i18n >= 3.20.0
Requires: python3-oslo-middleware >= 3.31.0
Requires: python3-oslo-messaging >= 14.1.0
Requires: python3-oslo-policy >= 3.7.0
Requires: python3-oslo-reports >= 1.18.0
Requires: python3-oslo-serialization >= 2.25.0
Requires: python3-oslo-service >= 1.24.0
Requires: python3-oslo-log >= 4.3.0
Requires: python3-oslo-versionedobjects >= 1.31.2
Requires: python3-debtcollector >= 1.19.0

Requires: python3-cinderclient >= 3.3.0
Requires: python3-glanceclient >= 1:2.8.0
Requires: python3-heatclient >= 1.10.0
Requires: python3-keystoneclient >= 1:3.8.0
Requires: python3-keystonemiddleware >= 5.1.0
Requires: python3-neutronclient >= 7.7.0
Requires: python3-novaclient >= 9.1.0
Requires: python3-swiftclient >= 3.2.0

Requires: python3-keystoneauth1 >= 3.18.0
Requires: python3-barbicanclient >= 4.5.2
Requires: python3-designateclient >= 2.7.0
Requires: python3-manilaclient >= 1.16.0
Requires: python3-openstackclient >= 3.12.0
Requires: python3-zaqarclient >= 1.3.0
Requires: python3-aodhclient >= 0.9.0
Requires: python3-octaviaclient >= 1.8.0
Requires: python3-ironicclient >= 2.8.0
%if 0%{rhosp} == 0
Requires: python3-magnumclient >= 2.3.0
Requires: python3-mistralclient >= 3.1.0
Requires: python3-monascaclient >= 1.12.0
Requires: python3-saharaclient >= 1.4.0
Requires: python3-troveclient >= 2.2.0
%endif
Requires: python3-openstacksdk >= 0.28.0
Requires: python3-tenacity >= 6.1.0

Requires: python3-yaml >= 5.1
Requires: python3-lxml >= 4.5.0
Requires: python3-migrate >= 0.13.0
Requires: python3-paste-deploy >= 1.5.0
Requires: python3-webob >= 1.7.1
Requires: python3-pytz >= 2013.6

Requires(pre): shadow-utils

%description common
Components common to all OpenStack Heat services

%files common -f %{service}.lang
%doc LICENSE
%{_bindir}/%{service}-manage
%{_bindir}/%{service}-status
%{_bindir}/%{service}-keystone-setup
%{_bindir}/%{service}-keystone-setup-domain
%{python3_sitelib}/%{service}
%{python3_sitelib}/openstack_%{service}-%{upstream_version}-*.egg-info
%exclude %{python3_sitelib}/%{service}/tests
%attr(-, root, %{service}) %{_datadir}/%{service}/%{service}-dist.conf
%dir %attr(0755,%{service},root) %{_localstatedir}/log/%{service}
%dir %attr(0755,%{service},root) %{_localstatedir}/run/%{service}
%dir %attr(0755,%{service},root) %{_sharedstatedir}/%{service}
%dir %attr(0755,%{service},root) %{_sysconfdir}/%{service}
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-%{service}
%config(noreplace) %attr(-, root, %{service}) %{_sysconfdir}/%{service}/api-paste.ini
%config(noreplace) %attr(-, root, %{service}) %{_sysconfdir}/%{service}/%{service}.conf
%config(noreplace) %attr(-,root,%{service}) %{_sysconfdir}/%{service}/environment.d/*
%config(noreplace) %attr(-,root,%{service}) %{_sysconfdir}/%{service}/templates/*
%if 0%{?with_doc}
%{_mandir}/man1/%{service}-keystone-setup.1.gz
%{_mandir}/man1/%{service}-keystone-setup-domain.1.gz
%{_mandir}/man1/%{service}-manage.1.gz
%{_mandir}/man1/%{service}-status.1.gz
%endif

%files -n python3-%{service}-tests
%license LICENSE
%{python3_sitelib}/%{service}/tests
%{python3_sitelib}/%{service}_integrationtests

%pre common
# 187:187 for heat - rhbz#845078
getent group %{service} >/dev/null || groupadd -r --gid 187 %{service}
getent passwd %{service}  >/dev/null || \
useradd --uid 187 -r -g %{service} -d %{_sharedstatedir}/%{service} -s /sbin/nologin \
-c "OpenStack Heat Daemons" %{service}
exit 0

%package engine
Summary: The Heat engine

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description engine
%{common_desc}

The %{service}-engine's main responsibility is to orchestrate the launching of
templates and provide events back to the API consumer.

%files engine
%doc README.rst LICENSE
%if 0%{?with_doc}
%doc doc/build/html/man/%{service}-engine.html
%endif
%{_bindir}/%{service}-engine
%{_unitdir}/openstack-%{service}-engine.service
%if 0%{?with_doc}
%{_mandir}/man1/%{service}-engine.1.gz
%endif

%post engine
%systemd_post openstack-%{service}-engine.service

%preun engine
%systemd_preun openstack-%{service}-engine.service

%postun engine
%systemd_postun_with_restart openstack-%{service}-engine.service


%package api
Summary: The Heat API

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description api
%{common_desc}

The %{service}-api component provides an OpenStack-native REST API that processes API
requests by sending them to the %{service}-engine over RPC.

%files api
%doc README.rst LICENSE
%if 0%{?with_doc}
%doc doc/build/html/man/%{service}-api.html
%endif
%{_bindir}/%{service}-api
%{_bindir}/%{service}-wsgi-api
%{_unitdir}/openstack-%{service}-api.service
%if 0%{?with_doc}
%{_mandir}/man1/%{service}-api.1.gz
%endif

%post api
%systemd_post openstack-%{service}-api.service

%preun api
%systemd_preun openstack-%{service}-api.service

%postun api
%systemd_postun_with_restart openstack-%{service}-api.service


%package api-cfn
Summary: Heat CloudFormation API

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description api-cfn
%{common_desc}

The %{service}-api-cfn component provides an AWS Query API that is compatible with
AWS CloudFormation and processes API requests by sending them to the
%{service}-engine over RPC.

%files api-cfn
%doc README.rst LICENSE
%if 0%{?with_doc}
%doc doc/build/html/man/%{service}-api-cfn.html
%endif
%{_bindir}/%{service}-api-cfn
%{_bindir}/%{service}-wsgi-api-cfn
%{_unitdir}/openstack-%{service}-api-cfn.service
%if 0%{?with_doc}
%{_mandir}/man1/%{service}-api-cfn.1.gz
%endif

%post api-cfn
%systemd_post openstack-%{service}-api-cfn.service

%preun api-cfn
%systemd_preun openstack-%{service}-api-cfn.service

%postun api-cfn
%systemd_postun_with_restart openstack-%{service}-api-cfn.service


%package monolith
Summary: The combined Heat engine/API

Requires: %{name}-common = %{epoch}:%{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description monolith
%{common_desc}

The %{service}-all process bundles together any (or all) of %{service}-engine,
%{service}-api, and %{service}-cfn-api into a single process. This can be used
to bootstrap a minimal TripleO deployment, but is not the recommended way of
running the Heat service in general.

%files monolith
%doc README.rst LICENSE
%{_bindir}/%{service}-all
%{_unitdir}/openstack-%{service}-all.service

%post monolith
%systemd_post openstack-%{service}-all.service

%preun monolith
%systemd_preun openstack-%{service}-all.service

%postun monolith
%systemd_postun_with_restart openstack-%{service}-all.service


%changelog
