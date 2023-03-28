# Guard for Red Hat OpenStack packaged modules
%global rhosp 0

Name:       openstack-puppet-modules
Epoch:      1
Version:    XXX
Release:    XXX
Summary:    Puppet modules to deploy OpenStack
License:    ASL 2.0

URL:        https://github.com/redhat-openstack/openstack-puppet-modules

BuildArch:  noarch

# For backward compatibility until we stop relying on OPM in TripleO
Requires:   puppet-tripleo

Requires:   puppet >= 2.7.0

%description
Metapackage for OpenStack Puppet Modules

%prep

%build

%install

%files

%changelog
