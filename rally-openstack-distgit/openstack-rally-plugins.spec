%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%global pname rally_openstack
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
rally-openstack is a collection of plugins for Rally framework \
designed for the OpenStack platform.

Name:             openstack-rally-plugins
Version:          XXX
Release:          XXX
Summary:          A collection of plugins for OpenStack Rally
License:          ASL 2.0
URL:              https://rally.readthedocs.io
Source0:          https://tarballs.openstack.org/rally-openstack/rally-openstack-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/rally-openstack/rally-openstack-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-setuptools
BuildRequires:    openstack-macros

# test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-ddt
BuildRequires:  python3-mock
BuildRequires:  python3-dateutil
BuildRequires:  python3-testtools
BuildRequires:  python3-kubernetes

Requires:       python3-rally
Requires:       python3-boto
Requires:       python3-gnocchiclient
Requires:       python3-keystoneauth1
Requires:       python3-os-faults
Requires:       python3-osprofiler
Requires:       python3-barbicanclient
Requires:       python3-cinderclient
Requires:       python3-designateclient
Requires:       python3-heatclient
Requires:       python3-glanceclient
Requires:       python3-ironicclient
Requires:       python3-keystoneclient
Requires:       python3-magnumclient
Requires:       python3-manilaclient
Requires:       python3-mistralclient
Requires:       python3-muranoclient
Requires:       python3-monascaclient
Requires:       python3-neutronclient
Requires:       python3-novaclient
Requires:       python3-octaviaclient
Requires:       python3-saharaclient
Requires:       python3-senlinclient
Requires:       python3-swiftclient
Requires:       python3-troveclient
Requires:       python3-zaqarclient
Requires:       python3-requests
Requires:       python3-kubernetes

%description
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -S git -n rally-openstack-%{upstream_version}

%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
# FIXME(chkumar246): watcherclient is not packaged in RDO
# So currently skipping the tests
%{__python3} -m pytest tests/unit || true

%files
%license LICENSE
%{python3_sitelib}/%{pname}
%{python3_sitelib}/%{pname}*.egg-info

%changelog
