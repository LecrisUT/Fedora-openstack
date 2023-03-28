%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
# add guard for OSP packages not carried
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-designate

Name:                   puppet-designate
Version:                9.5.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Designate
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-designate

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:              noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:               puppet-concat
Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-dns
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Designate (DNS Services).

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/designate/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/designate/



%files
%{_datadir}/openstack-puppet/modules/designate/


%changelog
* Thu Feb 02 2017 Alfredo Moralejo <amoralej@redhat.com> 9.5.0-1
- Update to 9.5.0



