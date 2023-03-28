%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name sensu-puppet
%global commit 7f60b2c5f708ed03b7769b69a1e86018db598aa9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-sensu
Version:        XXX
Release:        XXX
Summary:        A module to install the Sensu monitoring framework
License:        MIT

URL:            https://github.com/sensu/sensu-puppet

Source0:        https://github.com/sensu/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
A module to install the Sensu monitoring framework

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/sensu/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/sensu/



%files
%{_datadir}/openstack-puppet/modules/sensu/


%changelog

