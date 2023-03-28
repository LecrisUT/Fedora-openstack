
%global srcname tripleo_ansible
%global rolename tripleo-ansible

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible project for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/tripleo-ansible
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-jinja2 >= 2.8.0
BuildRequires:  python3-PyYAML
BuildRequires:  python3-metalsmith

Requires: (python3dist(ansible) >= 2.9.10 or ansible-core)
Requires: ansible-collections-openstack >= 1.3.0
Requires: ansible-collection-ansible-netcommon >= 1.5.0
Requires: ansible-collection-ansible-posix >= 1.2.0
Requires: ansible-collection-community-general >= 2.5.1
Requires: ansible-collection-containers-podman >= 1.4.1
Requires: ansible-config_template
Requires: ansible-role-collectd-config
Requires: ansible-role-metalsmith-deployment >= 1.2.0
Requires: ansible-role-openstack-operations
Requires: ansible-role-qdr-config
Requires: python3-jinja2 >= 2.8.0
Requires: python3-tripleo-common >= 16.0.0
Requires: python3-ironicclient
Requires: python3-glanceclient
Requires: python3-metalsmith >= 1.2.0
Requires: python3-heatclient

%description

Ansible project for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
