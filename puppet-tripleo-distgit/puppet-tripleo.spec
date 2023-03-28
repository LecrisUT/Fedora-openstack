%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
# add guard for OSP packages not carried
%global rhosp 0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-tripleo
Version:        XXX
Release:        XXX
Summary:        TripleO Puppet Module
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-tripleo

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-aodh >= 13.0.0
Requires:       puppet-apache
Requires:       puppet-barbican >= 13.0.0
Requires:       puppet-ceilometer >= 13.0.0
Requires:       puppet-cinder >= 13.0.0
Requires:       puppet-collectd
Requires:       puppet-concat
Requires:       puppet-designate >= 13.0.0
Requires:       puppet-etcd
Requires:       puppet-firewall
Requires:       puppet-glance >= 13.0.0
Requires:       puppet-gnocchi >= 13.0.0
Requires:       puppet-haproxy
Requires:       puppet-heat >= 13.0.0
Requires:       puppet-horizon >= 13.0.0
Requires:       puppet-inifile
Requires:       puppet-ironic >= 13.0.0
Requires:       puppet-keystone >= 13.0.0
Requires:       puppet-manila >= 13.0.0
Requires:       puppet-memcached
Requires:       puppet-module-data
Requires:       puppet-mysql
Requires:       puppet-neutron >= 13.0.0
Requires:       puppet-nova >= 13.0.0
Requires:       puppet-nssdb
Requires:       puppet-octavia >= 13.0.0
Requires:       puppet-openstacklib >= 13.0.0
Requires:       puppet-ovn >= 13.0.0
Requires:       puppet-oslo >= 13.0.0
Requires:       puppet-pacemaker
Requires:       puppet-placement
Requires:       puppet-qdr
Requires:       puppet-rabbitmq
Requires:       puppet-redis
Requires:       puppet-rsync
Requires:       puppet-rsyslog
Requires:       puppet-snmp
Requires:       puppet-ssh
Requires:       puppet-stdlib
Requires:       puppet-swift >= 13.0.0
Requires:       puppet-sysctl
Requires:       puppet-systemd
Requires:       puppet-vswitch >= 9.0.0
Requires:       puppet-xinetd
%if 0%{?fedora}
# NOTE(bogdando): only needed for f28-based CI passing,
# remove this condition for the "else" path, once we have Centos 8.
Requires:       puppet-headless >= 5.5.6
%else
Requires:       puppet-headless >= 5.5.10
%endif
# NOTE(aschultz): needed to properly manage firewall rules.
Requires:       iptables-services
%if 0%{?fedora} || 0%{?rhel} > 7
# NOTE(aschultz): needed for rabbitmq on rhel8/fedora, see LP#1822673
# https://review.openstack.org/#/c/649170/
Requires:       glibc-langpack-en
%endif

%description
Lightweight composition layer for Puppet TripleO.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n openstack-tripleo-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tripleo/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tripleo/



%files
%{_datadir}/openstack-puppet/modules/tripleo/


%changelog
