%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-module-data
%global commit 28dafce3a70b35364d33f64d9f518e1adffef242
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-module-data
Version:        XXX
Release:        XXX
Summary:        A hiera backend to allow the use of data while writing sharable modules
License:        ASL 2.0

URL:            https://github.com/ripienaar/puppet-module-data

Source0:        https://github.com/ripienaar/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
A hiera backend to allow the use of data while writing sharable modules

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data/



%files
%{_datadir}/openstack-puppet/modules/module-data/


%changelog


