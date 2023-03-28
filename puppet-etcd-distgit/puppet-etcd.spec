%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-etcd
Version:                XXX
Release:                XXX
Summary:                Installs and configures etcd
License:                ASL 2.0

URL:                    https://github.com/puppet-etcd/puppet-etcd

Source0:                https://github.com/puppet-etcd/puppet-etcd/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Installs and configures etcd

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/etcd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/etcd/



%files
%{_datadir}/openstack-puppet/modules/etcd/


%changelog
* Wed Oct 16 2019 Alan Bishop <abishop@redhat.com>
- Update URL to new offical location
