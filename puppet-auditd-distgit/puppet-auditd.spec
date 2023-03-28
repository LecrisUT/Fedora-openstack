%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-auditd
Version:                XXX
Release:                XXX
Summary:                Manage the audit daemon and it's rules.
License:                BSD

URL:                    https://github.com/kemra102/puppet-auditd

Source0:                https://github.com/kemra102/puppet-auditd/archive/%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-stdlib
Requires:               puppet-concat

Requires:               puppet >= 2.7.0

%description
This module handles installation of the auditd daemon, manages its main
configuration file as well as the user specified rules that auditd uses.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/auditd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/auditd/



%files
%{_datadir}/openstack-puppet/modules/auditd/


%changelog

