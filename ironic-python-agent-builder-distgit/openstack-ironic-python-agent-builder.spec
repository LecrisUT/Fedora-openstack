%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global rhosp 0

Name:           openstack-ironic-python-agent-builder
Summary:        Builder of ironic-python-agent ramdisk images
Version:        XXX
Release:        XXX
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://docs.openstack.org/ironic-python-agent-builder
Source0:        https://tarballs.openstack.org/ironic-python-agent-builder/ironic-python-agent-builder-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/ironic-python-agent-builder/ironic-python-agent-builder-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

%if 0%{?rhosp}
Epoch:		1
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       diskimage-builder >= 3.4.0

%description
This package contains a script to build an ironic-python-agent builder, as well
as a diskimage-builder element for it.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n ironic-python-agent-builder-%{upstream_version} -S git
# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%{py3_build}

%install
%{py3_install}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%license LICENSE
%doc README.rst
%doc AUTHORS
%doc ChangeLog
%{python3_sitelib}/ironic_python_agent_builder*
%{_bindir}/ironic-python-agent-builder
%{_datadir}/ironic-python-agent-builder

%changelog
