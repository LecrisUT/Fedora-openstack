%global srcname qdr_config_ansible_role

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources ansible-role-qdr-config}
%{!?dlrn: %global tarsources qdr-config-ansible-role}

Name:           ansible-role-qdr-config
Version:        XXX
Release:        XXX
Summary:        Ansible role for creating qdr configs

License:        ASL 2.0
URL:            https://github.com/infrawatch/qdr-config-ansible-role
Source0:        https://github.com/infrawatch/qdr-config-ansible-role/archive/%{upstream_version}/qdr-config-ansible-role-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core

Requires: (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible role for creating qdr configs

%prep
%autosetup -n %{tarsources}-%{upstream_version} -S git


%build


%install
mkdir -p  %{buildroot}%{_datadir}/ansible/roles/qdr_config
cp -r ./* %{buildroot}%{_datadir}/ansible/roles/qdr_config


%files
%doc README*
%license LICENSE
%{_datadir}/ansible/roles/qdr_config
%exclude %{_datadir}/ansible/role/qdr_config/tests/*

%changelog

