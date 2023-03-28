%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:           sahara-image-elements
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Image creation tools for Openstack Sahara

License:        ASL 2.0
URL:            https://launchpad.net/sahara
Source0:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr >= 2.0.0

Requires: dib-utils
Requires: diskimage-builder >= 2.11.0
Requires: rsync
Requires: wget
Requires: qemu-kvm
Requires: qemu-img
Requires: kpartx
Requires: git-core

%description
Sahara-image-elements provides the ability to create the images necessary to generate data processing clusters
in Sahara.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n sahara-image-elements-%{upstream_version}
# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%{py3_build}

%install
%{py3_install}

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/sahara-image-create
%{_bindir}/diskimage-create.sh
%{_datadir}/sahara-elements
%{python3_sitelib}/sahara_image_elements-%{upstream_version}-py%{python3_version}.egg-info

%changelog
