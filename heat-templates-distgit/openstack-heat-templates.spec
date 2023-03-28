%global commit b5e110ea90ebdcb75ec4beb954a918fb6d842ca4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git
%global project heat-templates

Name: openstack-heat-templates
Version: XXX
Release: XXX
Summary: Heat software config templates and DIB elements
License: ASL 2.0
URL: https://github.com/openstack/heat-templates
Source0: https://github.com/openstack/%{project}/archive/%{commit}.tar.gz#/%{project}-%{shortcommit}.tar.gz

BuildArch: noarch

%description
Heat software config templates and image building elements

%prep
%setup -qn %{project}-%{upstream_version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -aR hot/software-config %{buildroot}%{_datadir}/%{name}

# Use os-apply-config to bootstrap /etc/os-collect-config.conf
# from heat boot data
install -p -D -m 755 hot/software-config/boot-config/templates/fragments/20-os-apply-config %{buildroot}%{_libexecdir}/os-refresh-config/configure.d/20-os-apply-config
install -p -D -m 600 hot/software-config/boot-config/templates/fragments/os-collect-config.conf %{buildroot}%{_libexecdir}/os-apply-config/templates/etc/os-collect-config.conf 

# utilities which can be run by deployment scripts
install -p -D -m 755 hot/software-config/elements/heat-config/bin/heat-config-notify %{buildroot}/%{_bindir}/heat-config-notify
install -p -D -m 755 hot/software-config/elements/heat-config/bin/heat-config-rebuild-deployed %{buildroot}/%{_bindir}/heat-config-rebuild-deployed

# os-refresh-config script to run heat deployment resources
install -p -D -m 600 hot/software-config/elements/heat-config/os-apply-config/var/run/heat-config/heat-config %{buildroot}%{_libexecdir}/os-apply-config/templates/var/run/heat-config/heat-config
install -p -D -m 755 hot/software-config/elements/heat-config/os-refresh-config/configure.d/55-heat-config %{buildroot}%{_libexecdir}/os-refresh-config/configure.d/55-heat-config

# hook to perform configuration with scripts
install -p -D -m 755 hot/software-config/elements/heat-config-script/install.d/hook-script.py %{buildroot}%{_libexecdir}/heat-config/hooks/script

# hook to perform configuration with puppet
install -p -D -m 755 hot/software-config/elements/heat-config-puppet/install.d/hook-puppet.py %{buildroot}%{_libexecdir}/heat-config/hooks/puppet

# hook to perform configuration with ansible
install -p -D -m 755 hot/software-config/elements/heat-config-ansible/install.d/hook-ansible.py %{buildroot}%{_libexecdir}/heat-config/hooks/ansible

# hook to perform configuration with os-apply-config
install -p -D -m 755 hot/software-config/elements/heat-config-apply-config/install.d/hook-apply-config.py %{buildroot}%{_libexecdir}/heat-config/hooks/apply-config

# hook to perform configuration with hiera
install -p -D -m 755 hot/software-config/elements/heat-config-hiera/install.d/hook-hiera.py %{buildroot}%{_libexecdir}/heat-config/hooks/hiera

# hook to perform configuration with docker commands
install -p -D -m 755 hot/software-config/elements/heat-config-docker-cmd/os-refresh-config/configure.d/50-heat-config-docker-cmd %{buildroot}%{_libexecdir}/os-refresh-config/configure.d/50-heat-config-docker-cmd
install -p -D -m 755 hot/software-config/elements/heat-config-docker-cmd/install.d/hook-docker-cmd.py %{buildroot}%{_libexecdir}/heat-config/hooks/docker-cmd

# hook to generate json files
install -p -D -m 755 hot/software-config/elements/heat-config-json-file/install.d/hook-json-file.py %{buildroot}%{_libexecdir}/heat-config/hooks/json-file

%files
%license LICENSE
%doc README.rst
%{_datadir}/%{name}

%package -n python-heat-agent
Summary: Agent for performing Heat software deployments
Requires: python-heatclient
Requires: python-zaqarclient
Requires: heat-cfntools
Requires: os-collect-config
Requires: os-apply-config
Requires: os-refresh-config
Requires: dib-utils

%description -n python-heat-agent
This package installs and configures os-collect-config to allow Heat software
deployments to perform script based configuration tasks.

%files -n python-heat-agent
%license LICENSE
%{_bindir}/heat-config-notify
%{_bindir}/heat-config-rebuild-deployed
%{_libexecdir}/os-apply-config/templates/etc/os-collect-config.conf
%{_libexecdir}/os-apply-config/templates/var/run/heat-config/heat-config
%{_libexecdir}/os-refresh-config/configure.d/20-os-apply-config
%{_libexecdir}/os-refresh-config/configure.d/55-heat-config
%{_libexecdir}/heat-config/hooks/script

%package -n python-heat-agent-puppet
Summary: Agent for performing Puppet based Heat software deployments
Requires: python-heat-agent
Requires: puppet

%description -n python-heat-agent-puppet
This package installs and configures os-collect-config to allow Heat software
deployments to perform puppet based configuration tasks.

%files -n python-heat-agent-puppet
%license LICENSE
%{_libexecdir}/heat-config/hooks/puppet

%package -n python-heat-agent-ansible
Summary: Agent for performing Ansible based Heat software deployments
Requires: python-heat-agent
Requires: ansible

%description -n python-heat-agent-ansible
This package installs and configures os-collect-config to allow Heat software
deployments to perform ansible based configuration tasks.

%files -n python-heat-agent-ansible
%license LICENSE
%{_libexecdir}/heat-config/hooks/ansible

%package -n python-heat-agent-apply-config
Summary: Agent for performing os-apply-config based Heat software deployments
Requires: python-heat-agent
Requires: os-apply-config

%description -n python-heat-agent-apply-config
This package installs and configures os-collect-config to allow Heat software
deployments to perform os-apply-config based configuration tasks.

%files -n python-heat-agent-apply-config
%license LICENSE
%{_libexecdir}/heat-config/hooks/apply-config

%package -n python-heat-agent-hiera
Summary: Agent for performing hiera based Heat software deployments
Requires: python-heat-agent

%description -n python-heat-agent-hiera
This package installs and configures os-collect-config to allow Heat software
deployments to perform hiera based configuration tasks.

%files -n python-heat-agent-hiera
%license LICENSE
%{_libexecdir}/heat-config/hooks/hiera

%package -n python-heat-agent-docker-cmd
Summary: Agent for performing Docker based Heat software deployments
Requires: python-heat-agent
Requires: docker

%description -n python-heat-agent-docker-cmd
This package installs and configures os-collect-config to allow Heat software
deployments to perform docker based configuration tasks.

%files -n python-heat-agent-docker-cmd
%license LICENSE
%{_libexecdir}/heat-config/hooks/docker-cmd
%{_libexecdir}/os-refresh-config/configure.d/50-heat-config-docker-cmd

%package -n python-heat-agent-json-file
Summary: Agent for dumping data to JSON files
Requires: python-heat-agent

%description -n python-heat-agent-json-file
This package installs and configures os-collect-config to allow Heat software
deployments to generate json files.

%files -n python-heat-agent-json-file
%{_libexecdir}/heat-config/hooks/json-file

%changelog
