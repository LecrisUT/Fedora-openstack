%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-nssdb
%global commit 2e163a21fb80d828afede2d4be6214f1171c4887
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-nssdb
Version:        XXX
Release:        XXX
Summary:        NSS databse Puppet Module
License:        ASL 2.0

URL:            https://github.com/rcritten/puppet-nssdb

Source0:        http://github.com/rcritten/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
This Puppet Module manages NSS Databases.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb/


%files
%{_datadir}/openstack-puppet/modules/nssdb/


%changelog

