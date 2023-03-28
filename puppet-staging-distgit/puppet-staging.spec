%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-staging
%global commit b466d93f8deb0ed4d9762a17c3c38f356aa833ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-staging
Version:        XXX
Release:        XXX
Summary:        Compressed file staging and deployment
License:        ASL 2.0

URL:            https://github.com/nanliu/puppet-staging

Source0:        https://github.com/nanliu/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Compressed file staging and deployment

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/staging/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/staging/



%files
%{_datadir}/openstack-puppet/modules/staging/


%changelog


