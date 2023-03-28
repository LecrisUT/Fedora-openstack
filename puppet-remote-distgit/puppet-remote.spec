%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-remote
%global commit 35cc5571593d21408d625bd8ee35217345ec502a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-remote
Version:        XXX
Release:        XXX
Summary:        Remote Puppet Module
License:        ASL 2.0

URL:            https://github.com/paramite/puppet-remote

Source0:        http://github.com/paramite/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
This Puppet Module provides types and providers for managing
remote resources.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/remote/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/remote/



%files
%{_datadir}/openstack-puppet/modules/remote/


%changelog


