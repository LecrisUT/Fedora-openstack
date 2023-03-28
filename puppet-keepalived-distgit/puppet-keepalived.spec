%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-module-keepalived
%global commit bbca37ade629a9178f09366fd0368187fb645f4e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-keepalived
Version:        XXX
Release:        XXX
Summary:        Keepalived Puppet Module
License:        ASL 2.0

URL:            https://github.com/Unyonsys/puppet-module-keepalived

Source0:        http://github.com/Unyonsys/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
This Puppet Module manages keepalived instances.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/keepalived/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/keepalived/



%files
%{_datadir}/openstack-puppet/modules/keepalived/


%changelog


