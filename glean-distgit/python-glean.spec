%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global sname glean

%global common_desc \
Glean is a program intended to configure a system based on configuration \
provided in a configuration drive.

%global common_desc_tests Tests for Glean

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: Configure a system based on a configuration drive
License: ASL 2.0
URL: https://opendev.org/opendev/glean

Source0: http://tarballs.opendev.org/opendev/%{sname}/%{sname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.opendev.org/opendev/%{sname}/%{sname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch: noarch

BuildRequires: git-core
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary: Glean is a Python library to communicate with Redfish based systems
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: Glean tests
Requires: python3-%{sname} = %{version}-%{release}

BuildRequires: python3-oslotest
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires: python3-oslotest
Requires: python3-testrepository
Requires: python3-testscenarios
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc_tests}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: Glean documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for Glean
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{sname}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
%{__python3} setup.py build_sphinx
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%check
PYTHON=%{__python3} %{__python3} setup.py testr

%install
%{py3_install}
# Ensure proper permissions for scripts
chmod 755 %{buildroot}/%{python3_sitelib}/%{sname}/init/python-glean.template

%files -n python3-%{sname}
%license LICENSE
%{_bindir}/glean
%{_bindir}/glean-install
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.egg-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
