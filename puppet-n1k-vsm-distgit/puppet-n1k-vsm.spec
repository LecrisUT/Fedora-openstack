%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-n1k-vsm
%global commit 91772fa53dd3ed2686d2e8b0303c77ea6faefe68
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-n1k-vsm
Version:        XXX
Release:        XXX
Summary:        Puppet module for Cisco Nexus1000v VSM
License:        ASL 2.0

URL:            https://launchpad.net/puppet-n1k-vsm

Source0:        https://github.com/stackforge/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-vswitch
Requires:       puppet >= 2.7.0

%description
Puppet module for Cisco Nexus1000v VSM

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/n1k_vsm/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/n1k_vsm/



%files
%{_datadir}/openstack-puppet/modules/n1k_vsm/


%changelog

