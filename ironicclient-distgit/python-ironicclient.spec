%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname ironicclient

%global common_desc A python and command line client library for Ironic

Name:           python-ironicclient
Version:        XXX
Release:        XXX
Summary:        Python client for Ironic

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-%{sname}
Source0:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/python-%{sname}/python-%{sname}-%{version}%{?milestone}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif


%description
%{common_desc}


%package -n python3-%{sname}
Summary:        Python client for Ironic
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools

Requires:       xorriso
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-cliff >= 2.8.0
Requires:       python3-dogpile-cache >= 0.8.0
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.11.0
Requires:       python3-openstacksdk >= 0.18.0
Requires:       python3-osc-lib >= 2.0.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-yaml >= 3.13

%if 0%{?fedora} || 0%{?rhel} > 7
Suggests:       python3-openstackclient
%endif

%description -n python3-%{sname}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{name}-%{upstream_version}

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{_bindir}/baremetal
%{python3_sitelib}/%{sname}*
%{python3_sitelib}/python_%{sname}*

%changelog
