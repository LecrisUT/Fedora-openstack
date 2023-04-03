%global srcname %{name}
%global pypi_name ansible_pacemaker
%global commit 7c10fdb67b66bdb49f06545d35a4d5446b3aeb9c

Name:           ansible-pacemaker
Version:        1.0.4
Release:        %{autorelease}
Summary:        Ansible modules for managing Pacemaker clusters

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/%{name}
Source0:        https://github.com/redhat-openstack/%{name}/archive/%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel

Requires:       (python3dist(ansible) or ansible-core >= 2.11)
Requires:       python3-lxml

%description

Ansible-pacemaker is a set of Ansible modules for a Pacemaker cluster, nodes
and resources.

%prep
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
