%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


%global package_name networking-vsphere
%global srcname networking_vsphere

%define debug_package %{nil}

Name:       python-%{package_name}
Version:    XXX
Release:    XXX
Summary:    A set of Neutron drivers and agents to manage vSphere clusters.

License:    ASL 2.0
URL:        https://wiki.openstack.org/wiki/Neutron/Networking-vSphere

Source0:    https://tarballs.openstack.org/%{package_name}/%{package_name}-%{upstream_version}.tar.gz
Source1:    neutron-ovsvapp-agent.service

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-sphinx
BuildRequires:  rdo-rpm-macros
BuildRequires:  openstack-macros

Requires:   python-setuptools
Requires:   openstack-neutron-common
Requires:   python-oslo-vmware
Requires:   openvswitch

# Fix this owful shit when rootwrap/openvswitch-plugin.filters whould be
# available from common rpm for more beautiful requiring
Requires:  /usr/share/neutron/rootwrap/openvswitch-plugin.filters


%description
A set of Neutron drivers and agents to manage vSphere clusters.

* Free software: Apache license
* Source: http://git.openstack.org/cgit/openstack/networking-vsphere
* Bugs: https://bugs.launchpad.net/networking-vsphere

OVSvApp solution comprises of a service VM called OVSvApp VM hosted on each
ESXi hypervisor within a cluster and two vSphere Distributed Switches (VDS).

* Supports VLAN and VXLAN based networks.
* Security Groups.
* vMotion.

For help using or hacking on OVSvApp solution, you can send an email to the
`OpenStack Development Mailing List <mailto:openstack-dev@lists.openstack.org>`;
kindly use the [Networking-vSphere] Tag in the subject.

Getting started
https://wiki.openstack.org/wiki/Neutron/Networking-vSphere


%package -n neutron-ovsvapp-agent
Summary:   neutron-ovsvapp-agent related scripts and configs

Requires:  %name

%description -n neutron-ovsvapp-agent
neutron-ovsvapp-agent related scripts and configs


%package doc
Summary:   %{package_name} related documentation.

%description doc
%{package_name} related documentation.


%package nova
Summary:   A set for networking-vsphere nova drivers

Requires:  python-eventlet
Requires:  python-oslo-vmware
Requires:  python-nova

%description nova
A set for networking-vsphere nova drivers


%package tests
Summary:   A set of tests for %{package_name} package.

Requires:  python-sphinx
Requires:  python-hacking
Requires:  python-neutron-tests
Requires:  python-oslo-sphinx
Requires:  python-oslotest
Requires:  python-oslo-config
Requires:  python-oslo-vmware

%description tests
A set of tests for %{package_name} package.


%prep
%setup -q -n %{package_name}-%{upstream_version}

export PBR_VERSION=%{version}

# Let's handle dependencies ourseleves
%py_req_cleanup


%build
%py2_build


%install
%py2_install
%{__python2} setup.py build_sphinx -b man

# Move config file to proper location
mkdir -p %{buildroot}%{_sysconfdir}/neutron/
mv %{buildroot}%{_prefix}/etc/neutron/ %{buildroot}%{_sysconfdir}/

# Don't pack patch for python-nova
rm -f %{buildroot}%{_prefix}/var/tmp/nova.patch

# Install systemd-unit for service
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/neutron-ovsvapp-agent.service


%files
%{_bindir}/*
%{python2_sitelib}/%{srcname}*

%exclude %{python2_sitelib}/%{srcname}/tests/
%exclude %{python2_sitelib}/%{srcname}/nova/virt/vmwareapi/
%exclude %{_unitdir}/neutron-ovsvapp-agent.service
%exclude %{_sysconfdir}/neutron/*.ini
%exclude %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files -n neutron-ovsvapp-agent
%{_unitdir}/neutron-ovsvapp-agent.service
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/*.ini
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini


%files doc
%license LICENSE
%doc doc/build/man


%files nova
%{python2_sitelib}/%{srcname}/nova/virt/vmwareapi/*


%files tests
%{python2_sitelib}/%{srcname}/tests/*


%post
%systemd_post neutron-ovsvapp-agent.service

ovsmon_dir=%{_localstatedir}/log/neutron/ovsvapp-agent/
[ -d $ovsmon_dir ] || mkdir $ovsmon_dir && chown neutron:neutron $ovsmon_dir


%preun
%systemd_preun neutron-ovsvapp-agent.service


%changelog
* Fri Oct 21 2016 Vladislav Odintsov <odivlad@gmail.com> - 2.0.1-1
- Initial package.
