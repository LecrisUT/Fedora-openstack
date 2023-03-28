%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{!?upstream_name: %global upstream_name openstack-tacker}

Name:                   puppet-tacker
Version:                XXX
Release:                XXX
Summary:                Puppet module for OpenStack Tacker
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-tacker

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:              noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-keystone
Requires:               puppet-oslo

Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Tacker.

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
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tacker/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tacker/



%files
%{_datadir}/openstack-puppet/modules/tacker/


%changelog
* Mon Jan 09 2017 Dan Radez <dradez@redhat.com> - XXX-XXX
- Initial Packaging

