%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-tomcat
%global commit c8c66135f7140b91a2bb4e59672a067678cfa782
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-tomcat
Version:        XXX
Release:        XXX
Summary:        Installs, deploys, and configures Apache Tomcat web services.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-tomcat

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet-staging
Requires:       puppet >= 2.7.0

%description
Installs, deploys, and configures Apache Tomcat web services.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tomcat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tomcat/



%files
%{_datadir}/openstack-puppet/modules/tomcat/


%changelog


