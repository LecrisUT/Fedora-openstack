%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-kibana3
%global commit 6ca9631fbe82766134f98e2e8780bb91e7cd3f0e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-kibana3
Version:        XXX
Release:        XXX
Summary:        Installs and configures kibana3.
License:        ASL 2.0

URL:            https://github.com/thejandroman/puppet-kibana3

Source0:        https://github.com/thejandroman/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-git
Requires:       puppet-vcsrepo
Requires:       puppet-apache
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs and configures kibana3.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/kibana3/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/kibana3/



%files
%{_datadir}/openstack-puppet/modules/kibana3/


%changelog


