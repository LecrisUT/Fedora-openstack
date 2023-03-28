%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name konstantin-fluentd
%global commit 0400aafa8f23971485b838750d41928585cf3547
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-fluentd
Version:        XXX
Release:        XXX
Summary:        Installs, configures, and manages Fluentd data collector
License:        ASL 2.0

URL:            https://github.com/soylent/konstantin-fluentd

Source0:        https://github.com/soylent/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages Fluentd data collector

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
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/fluentd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/fluentd/



%files
%{_datadir}/openstack-puppet/modules/fluentd/


%changelog


