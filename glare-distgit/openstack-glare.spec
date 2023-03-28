%global service glare

# oslosphinx do not work with sphinx > 2
%global with_doc 0

%global common_desc \
OpenStack Glare provides API for catalog of binary data along with its metadata.

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             openstack-%{service}
Version:          XXX
Release:          XXX
Summary:          Glare Artifact Repository
License:          ASL 2.0
URL:              https://github.com/openstack/%{service}
BuildArch:        noarch
Source0:          http://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
Source1:          %{service}.logrotate

Source10:         %{name}-api.service
Source11:         %{name}-scrubber.service

BuildRequires:    git-core
BuildRequires:    intltool
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-setuptools
BuildRequires:    openstack-macros
BuildRequires:    systemd
# Required for config generation
BuildRequires:    python3-alembic
BuildRequires:    python3-cryptography
BuildRequires:    python3-cursive
BuildRequires:    python3-eventlet
BuildRequires:    python3-futurist
BuildRequires:    python3-glance-store
BuildRequires:    python3-iso8601
BuildRequires:    python3-jsonpatch
BuildRequires:    python3-jsonschema
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-keystoneclient
BuildRequires:    python3-keystonemiddleware
BuildRequires:    python3-microversion-parse
BuildRequires:    python3-os-brick
BuildRequires:    python3-oslo-concurrency
BuildRequires:    python3-oslo-config
BuildRequires:    python3-oslo-context
BuildRequires:    python3-oslo-db-tests
BuildRequires:    python3-oslo-i18n
BuildRequires:    python3-oslo-log
BuildRequires:    python3-oslo-messaging
BuildRequires:    python3-oslo-middleware
BuildRequires:    python3-oslo-policy
BuildRequires:    python3-oslo-serialization
BuildRequires:    python3-oslo-service
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-oslo-versionedobjects
BuildRequires:    python3-oslo-vmware
BuildRequires:    python3-osprofiler
BuildRequires:    python3-pbr
BuildRequires:    python3-routes
BuildRequires:    python3-six
BuildRequires:    python3-sqlalchemy
BuildRequires:    python3-swiftclient
BuildRequires:    python3-taskflow
BuildRequires:    python3-webob
BuildRequires:    python3-pyOpenSSL
# Required for tests
BuildRequires:    python3-stestr
BuildRequires:    python3-oslotest
BuildRequires:    python3-testrepository
BuildRequires:    python3-testscenarios
BuildRequires:    python3-testtools
BuildRequires:    python3-mock

BuildRequires:    python3-httplib2
BuildRequires:    python3-jwt
BuildRequires:    python3-memcached
BuildRequires:    python3-monotonic
BuildRequires:    python3-paste
BuildRequires:    python3-paste-deploy
BuildRequires:    python3-retrying
BuildRequires:    python3-semantic_version
BuildRequires:    python3-requests-mock


%description
Glare Artifact Repository


%package -n       python3-%{service}
Summary:          OpenStack Glare python libraries
%{?python_provide:%python_provide python3-%{service}}


Requires:         python3-alembic >= 0.8.10
Requires:         python3-cryptography >= 1.9
Requires:         python3-eventlet >= 0.18.2
Requires:         python3-futurist >= 1.2.0
Requires:         python3-glance-store >= 0.22.0
Requires:         python3-iso8601 >= 0.1.11
Requires:         python3-jsonpatch >= 1.16
Requires:         python3-jsonschema >= 2.6.0
Requires:         python3-keystoneauth1 >= 3.3.0
Requires:         python3-keystoneclient >= 1:3.8.0
Requires:         python3-keystonemiddleware >= 4.17.0
Requires:         python3-microversion-parse >= 0.1.2
Requires:         python3-os-brick >= 1.8.0
Requires:         python3-oslo-concurrency >= 3.20.0
Requires:         python3-oslo-config >= 2:5.1.0
Requires:         python3-oslo-context >= 2.19.2
Requires:         python3-oslo-db >= 4.27.0
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-log >= 3.30.0
Requires:         python3-oslo-messaging >= 5.29.0
Requires:         python3-oslo-middleware >= 3.31.0
Requires:         python3-oslo-policy >= 1.23.0
Requires:         python3-oslo-serialization >= 2.18.0
Requires:         python3-oslo-service >= 1.24.0
Requires:         python3-oslo-utils >= 3.31.0
Requires:         python3-oslo-versionedobjects >= 1.28.0
Requires:         python3-oslo-vmware >= 0.11.1
Requires:         python3-osprofiler >= 1.4.0
Requires:         python3-pbr >= 2.0.0
Requires:         python3-routes >= 2.3.1
Requires:         python3-six >= 1.10.0
Requires:         python3-sqlalchemy >= 1.0.10
Requires:         python3-swiftclient >= 2.2.0
Requires:         python3-taskflow >= 2.7.0
Requires:         python3-webob >= 1.7.1
Requires:         python3-wsme >= 0.8.0
Requires:         python3-pyOpenSSL >= 16.2.0

Requires:         python3-httplib2 >= 0.9.1
Requires:         python3-jwt >= 1.6.0
Requires:         python3-memcached >= 1.56
Requires:         python3-paste
Requires:         python3-paste-deploy >= 1.5.0
Requires:         python3-retrying >= 1.2.3
Requires:         python3-semantic_version >= 2.3.1

#test deps: python-mox python-nose python-requests
#test and optional store:
#ceph - glance_store.rdb
#python-boto - glance_store.s3
Requires:         python3-boto

Requires(pre):    shadow-utils

%description -n   python3-glare
%{common_desc}

This package contains the Glare python library.

%package        common
Summary:        Components common to all OpenStack glare services

Requires:       python3-glare = %{version}-%{release}

%description    common
%{common_desc}

%package        api

Summary:        OpenStack Glare api

Requires:       %{name}-common = %{version}-%{release}

%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description api
%{common_desc}

This package contains the Glare API service.


%package -n python3-glare-tests
Summary:        Glare tests
%{?python_provide:%python_provide python3-glare-tests}
Requires:       python3-glare = %{version}-%{release}
Requires:       python3-tempest

%description -n python3-glare-tests
%{common_desc}

This package contains the Glare test files.

%if 0%{?with_doc}
%package        doc

Summary:        Documentation for OpenStack Artifact Service

BuildRequires:    python3-sphinx
BuildRequires:    python3-oslo-sphinx
BuildRequires:    python3-eventlet
BuildRequires:    python3-jsonschema
BuildRequires:    python3-keystoneclient
BuildRequires:    python3-keystonemiddleware
BuildRequires:    python3-oslo-db
BuildRequires:    python3-oslo-log
BuildRequires:    python3-oslo-messaging
BuildRequires:    python3-oslo-policy
BuildRequires:    python3-osprofiler
BuildRequires:    python3-sphinxcontrib-httpdomain

%description    doc
%{common_desc}

This package contains Openstack Glare documentation
%endif


%prep
%autosetup -n %{service}-%{upstream_version} -S git

find . \( -name .gitignore -o -name .placeholder \) -delete

find glare -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%py_req_cleanup


%build
# Generate config file
PYTHONPATH=. oslo-config-generator --config-file=etc/oslo-config-generator/glare.conf
# Generate oslo policies
PYTHONPATH=. oslopolicy-sample-generator-3 --namespace=glare --output-file=etc/policy.yaml.sample
PYTHONPATH=. sed -i 's/^#"//' etc/policy.yaml.sample
%{py3_build}

%install
%{py3_install}

%if 0%{?with_doc}
%{__python3} setup.py build_sphinx -b html
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

# Install config files
install -p -D -m 644 etc/glare.conf.sample %{buildroot}%{_sysconfdir}/glare/glare.conf
install -p -D -m 644 etc/policy.yaml.sample %{buildroot}%{_sysconfdir}/glare/policy.yaml
install -p -D -m 644 etc/glare-paste.ini %{buildroot}%{_sysconfdir}/glare/glare-paste.ini
install -p -D -m 644 etc/glare-swift.conf.sample %{buildroot}%{_sysconfdir}/glare/glare-swift.conf

# Setup directories
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare
install -d -m 755 %{buildroot}%{_sharedstatedir}/glare/artifacts
install -d -m 755 %{buildroot}%{_localstatedir}/log/glare

# Install systemd unit services
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-api.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/%{name}-scrubber.service

# Logrotate config
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Remove unused files
rm -f %{buildroot}/usr/etc/glare/*

# Create fake egg-info for the tempest plugin
%py3_entrypoint %{service} %{service}

%pre common
getent group glare >/dev/null || groupadd -r glare
if ! getent passwd glare >/dev/null; then
  useradd -r -g glare -G glare -d %{_sharedstatedir}/glare -s /sbin/nologin -c "OpenStack Glare daemon" glare
fi
exit 0

%post api
# Initial installation
%systemd_post %{name}-api.service
%systemd_post %{name}-scrubber.service

%preun api
%systemd_preun %{name}-api.service
%systemd_preun %{name}-scrubber.service

%postun api
%systemd_postun_with_restart %{name}-api.service
%systemd_postun_with_restart %{name}-scrubber.service


%check
PYTHON=%{__python3} stestr run --black-regex 'glare.tests.unit.test_unpacking.TestArtifactHooks.test_unpacking_database_big_archive|glare.tests.unit.test_unpacking.TestArtifactHooks.test_unpacking_big_archive' || true


%files -n python3-glare
%license LICENSE
%doc README.rst
%{python3_sitelib}/glare
%{python3_sitelib}/glare-*.egg-info
%exclude %{python3_sitelib}/glare/tests
%exclude %{python3_sitelib}/glare_tempest_plugin

%files -n python3-glare-tests
%{python3_sitelib}/glare/tests
%{python3_sitelib}/glare_tempest_plugin
%{python3_sitelib}/%{service}_tests.egg-info

%files common
%dir %{_sysconfdir}/glare
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare.conf
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/policy.yaml
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-paste.ini
%config(noreplace) %attr(-, root, glare) %{_sysconfdir}/glare/glare-swift.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(0755, glare, root)  %{_localstatedir}/log/glare

%defattr(-, glare, glare, -)
%dir %{_sharedstatedir}/glare
%dir %{_sharedstatedir}/glare/artifacts

%files api
%{_bindir}/glare-api
%{_bindir}/glare-db-manage
%{_bindir}/glare-scrubber
%{_unitdir}/%{name}-api.service
%{_unitdir}/%{name}-scrubber.service

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
