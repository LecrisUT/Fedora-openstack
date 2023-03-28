%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}}

Name:           python-dracclient
Version:        XXX
Release:        XXX
Summary:        Library for managing machines with Dell iDRAC cards.

License:        ASL 2.0
URL:            http://github.com/openstack/%{name}
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif


BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
Library for managing machines with Dell iDRAC cards.

%package -n     python3-dracclient
Summary:        Library for managing machines with Dell iDRAC cards.
%{?python_provide:%python_provide python3-dracclient}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# All this is required to run unit tests in check phase
BuildRequires:  python3-mock
BuildRequires:  python3-requests

BuildRequires:  python3-lxml
BuildRequires:  python3-requests-mock

Requires: python3-requests

Requires: python3-lxml

%description -n     python3-dracclient
Library for managing machines with Dell iDRAC cards.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{name}.egg-info
# Let RPM handle the dependencies
rm -f {test-,}requirements.txt

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} -m unittest discover dracclient.tests

%files -n     python3-dracclient
%doc README.rst LICENSE
%{python3_sitelib}/dracclient*
%{python3_sitelib}/python_dracclient*

%changelog
