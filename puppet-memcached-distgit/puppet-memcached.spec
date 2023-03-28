%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-memcached
%global commit bfa64e066a709cae8bed12ff95e9d630ad50af14
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-memcached
Version:        XXX
Release:        XXX
Summary:        Manage memcached via Puppet
License:        ASL 2.0

URL:            https://github.com/saz/puppet-memcached

Source0:        https://github.com/saz/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-firewall
Requires:       puppet >= 2.7.0

%description
Manage memcached via Puppet

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
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/memcached/



%files
%{_datadir}/openstack-puppet/modules/memcached/


%changelog


