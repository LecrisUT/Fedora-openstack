%global srcname tripleo_powerflex
%global rolename tripleo-powerflex

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role for setting up PowerFlex for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/dell/tripleo-powerflex
Source0:        https://github.com/dell/tripleo-powerflex/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git-core

Requires:       (python3dist(ansible) or ansible-core >= 2.11)
Requires:       openstack-tripleo-heat-templates

%description

Ansible role to configure PowerFlex for TripleO

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build


%install
mkdir -p  %{buildroot}%{_datadir}/ansible/roles/
cp -r tripleo-powerflex-run-ansible %{buildroot}%{_datadir}/ansible/roles/
cp -r powerflex-ansible %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/environments
mkdir -p  %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/deployment
cp -r templates/overcloud/environments/powerflex-ansible %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/environments
cp -r templates/overcloud/deployment/powerflex-ansible %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/deployment


%files
%doc README*
%license LICENSE
%{_datadir}/ansible/roles/tripleo-powerflex-run-ansible
%{_datadir}/powerflex-ansible
%{_datadir}/openstack-tripleo-heat-templates/environments/powerflex-ansible
%{_datadir}/openstack-tripleo-heat-templates/deployment/powerflex-ansible


%changelog

