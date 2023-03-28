%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-barometer
Version:        XXX
Release:        XXX
Summary:        Scripts for Barometer deployment on using Apex

License:        ASL 2.0
URL:            https://wiki.opnfv.org/display/fastpath/
Source0:        https://github.com/opnfv/puppet-barometer/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet-java
Requires:       puppet >= 2.7.0

%description
Puppet module that installs and configures the Barometer.

%prep
%setup -q -n %{name}-%{version}
find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/barometer
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/barometer


%files
%{_datadir}/openstack-puppet/modules/barometer



%changelog
