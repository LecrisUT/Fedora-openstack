%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name puppet-powerdns
%global commit 899651549b6d57470d233321265ace862270e154
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-powerdns
Version:                XXX
Release:                XXX
Summary:                Module for managing PowerDNS
License:                GPLv2

URL:                    https://github.com/antonlindstrom/puppet-powerdns

Source0:                https://github.com/antonlindstrom/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Puppet module to install and configure PowerDNS

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/powerdns/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/powerdns/



%files
%{_datadir}/openstack-puppet/modules/powerdns/


%changelog

