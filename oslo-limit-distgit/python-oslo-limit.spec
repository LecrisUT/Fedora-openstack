%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1}}
%global sources_gpg_sign 0x4c29ff0e437f3351fd82bdf47c5a3bc787dc7035
%global pypi_name oslo.limit
%global pkg_name oslo-limit
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Oslo.limit is the limit enforcement library to assist with quota \
calculation. It aims to provide support for quota \
enforcement across all OpenStack services.

Name:           python-%{pkg_name}
Version:        XXX
Release:        XXX
Summary:        Limit enforcement library to assist with quota calculation

License:        ASL 2.0
URL:            https://docs.openstack.org/oslo.limit/latest/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:      https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:      https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

BuildRequires: git

%description
%{common_desc}

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.9.0
BuildRequires:  python3-openstacksdk >= 0.31.1
BuildRequires:  python3-oslo-config >= 5.2.0
BuildRequires:  python3-oslo-i18n >= 3.15.3
BuildRequires:  python3-oslo-log >= 3.44.0
BuildRequires:  python3-oslotest >= 3.2.0
BuildRequires:  python3-stestr

Requires:       python3-keystoneauth1 >= 3.9.0
Requires:       python3-openstacksdk >= 0.31.1
Requires:       python3-oslo-config >= 5.2.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.44.0

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:        oslo.limit documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-%{pkg_name}-doc
Documentation for oslo.limit library.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let RPM handle the requirements
rm -f {test-,}requirements.txt

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%if 0%{?with_doc}
# generate html docs
PYTHONPATH=${PWD} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
stestr run

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_limit
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
