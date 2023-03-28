%{!?upstream_version: %global upstream_version %{commit}}

%define upstream_name puppet-dns
%global commit 162d17309e4bbea6bcd0a51c25275ea9e5f98fdf
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-dns
Version:                XXX
Release:                XXX
Summary:                Manage the ISC BIND daemon
License:                Apache-2.0

URL:                    https://github.com/theforeman/puppet-dns

Source0:                https://github.com/theforeman/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-concat
Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Puppet module for configuring the ISC BIND server for Foreman.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/dns/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/dns/



%files
%{_datadir}/openstack-puppet/modules/dns/


%changelog

