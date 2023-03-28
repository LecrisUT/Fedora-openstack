%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-sysctl
%global commit 65ffe839a4ce785bc3901452488197a0ef158cd8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-sysctl
Version:        XXX
Release:        XXX
Summary:        This modules allows you to configure sysctl.
License:        GPL-2.0

URL:            https://github.com/duritong/puppet-sysctl

Source0:        https://github.com/duritong/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
This modules allows you to configure sysctl.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl/



%files
%{_datadir}/openstack-puppet/modules/sysctl/


%changelog


