%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-lib-file_concat
Version:                1.0.1
Release:                1%{?dist}
Summary:                Library for concatenating multiple files into 1
License:                ASL 2.0

URL:                    https://github.com/electrical/puppet-lib-file_concat

Source0:                https://github.com/electrical/puppet-lib-file_concat/archive/%{version}.tar.gz

BuildArch:              noarch


Requires:               puppet >= 2.7.0

%description
Library for concatenating multiple files into 1

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/file_concat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/file_concat/



%files
%{_datadir}/openstack-puppet/modules/file_concat/


%changelog
* Tue Dec 13 2016 Alejandro Andreu <alejandroandreu@openmailbox.org> 1.0.1-1
- Initial specfile

