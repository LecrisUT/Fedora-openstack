%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-datacat
%global commit 10f6dde9a3c3c47c06a6322d22d7723685d9976a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-datacat
Version:        XXX
Release:        XXX
Summary:        Puppet type for handling data fragments
License:        ASL 2.0

URL:            https://github.com/richardc/puppet-datacat

Source0:        http://github.com/richardc/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Puppet type for handling data fragments

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/datacat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/datacat/



%files
%{_datadir}/openstack-puppet/modules/datacat/


%changelog


