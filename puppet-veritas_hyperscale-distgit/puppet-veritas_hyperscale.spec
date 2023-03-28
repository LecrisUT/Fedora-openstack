%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-veritas_hyperscale
Version:                1.1.1
Release:                1%{?dist}
Summary:                Veritas HyperScale installer.
License:                ASL 2.0

URL:                    https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale

Source0:                https://github.com/vtas-hyperscale-ci/puppet-veritas_hyperscale/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-rabbitmq
Requires:               puppet-keystone
Requires:               puppet-nova
Requires:               puppet-cinder
Requires:               puppet-openstacklib

Requires:               puppet >= 2.7.0

%description
Installs and configures Veritas Hyperscale (Controller).

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/veritas_hyperscale/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/veritas_hyperscale/



%files
%{_datadir}/openstack-puppet/modules/veritas_hyperscale/


%changelog
* Wed Dec 20 2017 RDO <dev@lists.rdoproject.org> 1.1.1-1
- Update to 1.1.1

* Wed Dec 13 2017 RDO <dev@lists.rdoproject.org> 1.1.0-1
- Update to 1.1.0

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-1
- Update to 1.0.0

