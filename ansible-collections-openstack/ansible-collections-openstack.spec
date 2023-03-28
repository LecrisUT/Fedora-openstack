%global pypi_name ansible-collections-openstack.cloud
%global srcname %{pypi_name}

Name:           ansible-collections-openstack
Version:        2.0.0
Release:        %autorelease
Summary:        Openstack Ansible collections
License:        GPLv3+
URL:            https://opendev.org/openstack/%{name}
Source0:        https://galaxy.ansible.com/download/openstack-cloud-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

Requires:       (ansible >= 2.8.0 or ansible-core >= 2.11)
Requires:       python3-openstacksdk >= 0.13.0

%description

Openstack Ansible collections

%prep
%autosetup -n %{srcname}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install
%pyproject_save_files %{pypi_name}

%files
%doc README.md
%license COPYING
%{python3_sitelib}/%{pypi_name}-*.egg-info
%{_datadir}/ansible/collections/ansible_collections/openstack/cloud/

%changelog
%autochangelog
