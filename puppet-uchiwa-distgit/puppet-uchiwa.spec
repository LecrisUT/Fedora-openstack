%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-uchiwa
%global commit 64ce619c26995bc270aa762e24ca298b9787bc3e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-uchiwa
Version:        XXX
Release:        XXX
Summary:        Puppet module for installing Uchiwa
License:        ASL 2.0

URL:            https://github.com/yelp/puppet-uchiwa

Source0:        https://github.com/Yelp/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for installing Uchiwa

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/uchiwa/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/uchiwa/



%files
%{_datadir}/openstack-puppet/modules/uchiwa/


%changelog


