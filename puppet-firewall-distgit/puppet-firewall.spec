%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-firewall
%global commit e70157ef0692b679470a980d7051c4b73000ed9f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-firewall
Version:        XXX
Release:        XXX
Summary:        Manages Firewalls such as iptables
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-firewall

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Manages Firewalls such as iptables

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall/



%files
%{_datadir}/openstack-puppet/modules/firewall/


%changelog
