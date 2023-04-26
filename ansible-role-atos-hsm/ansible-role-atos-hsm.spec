%global srcname %{name}
%global pypi_name ansible_role_atos_hsm
%global rolename ansible-role-atos-hsm
%global sources_gpg_sign 0xa7475c5f2122fec3f90343223fe3bf5aad1080e4

Name:           ansible-role-atos-hsm
Version:        5.0.0
Release:        %{autorelease}
Summary:        Ansible role for configuring ATOS HSM Clients

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
Source101:      https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  git-core
BuildRequires:  python3-devel

Requires:       (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible role to configure ATOS HSM clients

%prep
# Required for tarball sources verification
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install
%pyproject_save_files %{pypi_name}

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{_datadir}/ansible/roles/

%changelog
%autochangelog
