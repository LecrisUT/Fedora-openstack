%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?upstream_name: %global upstream_name openstack-congress}

Name:                   puppet-congress
Version:                XXX
Release:                XXX
Summary:                Puppet module for OpenStack Congress
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-congress

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet-keystone

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Congress.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/congress/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/congress/



%files
%{_datadir}/openstack-puppet/modules/congress/


%changelog
* Mon Jan 09 2017 Dan Radez <dradez@redhat.com> - XXX-XXX
- Initial Packaging

