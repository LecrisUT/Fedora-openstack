%global srcname %{name}
%global pypi_name ansible_config_template
%global sources_gpg_sign 0xa63ea142678138d1bb15f2e303bdfd64dd164087

Name:           ansible-config_template
Version:        2.0.0
Release:        %{autorelease}
Summary:        Ansible plugin for config template

License:        ASL 2.0
URL:            https://opendev.org/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
Source101:      https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt

BuildArch:      noarch

# Required for tarball sources verification
BuildRequires:  gnugpg2
BuildRequires:  git-core
BuildRequires:  python3-devel

Requires:       (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible plugin for config template

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
%doc README*
%license LICENSE
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{_datadir}/ansible/

%changelog
%autochangelog
