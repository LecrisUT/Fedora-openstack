%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

# guard for package OSP does not support
%global rhosp 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           openstack-tripleo-heat-templates
Summary:        Heat templates for TripleO
Version:        XXX
Release:        XXX
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       ansible-pacemaker
Requires:       ansible-tripleo-ipsec
Requires:       ansible-role-atos-hsm
Requires:       ansible-role-container-registry
Requires:       ansible-role-chrony
Requires:       ansible-role-lunasa-hsm
Requires:       ansible-role-thales-hsm
Requires:       python3-jinja2
Requires:       openstack-tripleo-common >= 7.1.0
Requires:       tripleo-ansible >= 1.1.0
Requires:       python3-PyYAML
Requires:       rhel-system-roles
%if 0%{rhosp} == 1
Requires:       ansible-role-redhat-subscription
%endif

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n tripleo-heat-templates-%{upstream_version}
# Replace "env python" shebag to the correct python executable for the system
# if we don't do that brp-mangle-shebangs will change it to python2
for python_script in $(grep "/usr/bin/env python" . -rl)
do
    sed -i "s#/usr/bin/env python.*#%{__python3}#g" $python_script
done

%build
%{py3_build}

%install
%{py3_install}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}
cp -ar common %{buildroot}/%{_datadir}/%{name}
if [ -d docker ] ; then
  cp -ar docker %{buildroot}/%{_datadir}/%{name}
fi
cp -ar deployment %{buildroot}/%{_datadir}/%{name}

# docker_config_scripts will be removed in Stein
if [ -d docker_config_scripts ]; then
  cp -ar docker_config_scripts %{buildroot}/%{_datadir}/%{name}
fi
if [ -d container_config_scripts ]; then
  cp -ar container_config_scripts %{buildroot}/%{_datadir}/%{name}
fi
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}
cp -ar network %{buildroot}/%{_datadir}/%{name}
if [ -d networks ]; then
  cp -ar networks %{buildroot}/%{_datadir}/%{name}
fi
if [ -d network-data-samples ]; then
  cp -ar network-data-samples %{buildroot}/%{_datadir}/%{name}
fi
if [ -d baremetal-samples ]; then
  cp -ar baremetal-samples %{buildroot}/%{_datadir}/%{name}
fi
if [ -d validation-scripts ]; then
  cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}
fi
cp -ar deployed-server %{buildroot}/%{_datadir}/%{name}
cp -ar ci %{buildroot}/%{_datadir}/%{name}
cp -ar roles %{buildroot}/%{_datadir}/%{name}
cp -ar scripts %{buildroot}/%{_datadir}/%{name}
cp -ar tools %{buildroot}/%{_datadir}/%{name}
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{python3_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python3_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

%files
%doc README*
%license LICENSE
%{python3_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}

%changelog
