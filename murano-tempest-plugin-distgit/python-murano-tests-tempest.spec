%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%global service murano
%global plugin murano-tempest-plugin
%global module murano_tempest_tests
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the murano project. \
Additionally it provides a plugin to automatically load these tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Murano Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Obsoletes:   python-murano-tests < 5.0.0

Requires:   python3-pbr >= 3.1.1
Requires:   python3-six >= 1.10.0
Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-testtools >= 2.2.0
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-utils >= 3.33.0
Requires:   python3-requests >= 2.14.2
Requires:   python3-testresources
Requires:   python3-keystoneclient
Requires:   python3-heatclient
Requires:   python3-neutronclient
Requires:   python3-muranoclient
Requires:   python3-mistralclient

%description -n python3-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{service}-tests-tempest-doc
Summary:        python-%{service}-tests-tempest documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{service}-tests-tempest-doc
It contains the documentation for the murano tempest plugin.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

# Generate Docs
%if 0%{?with_doc}
sphinx-build -b html doc/source doc/build/html
# remove the sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{service}-tests-tempest-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog

