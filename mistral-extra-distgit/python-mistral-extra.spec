%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
%global rhosp 0

%global library mistral-extra
%global module mistral_extra

%global common_desc Python library containting Mistral actions

Name:       python-%{library}
Version:    XXX
Release:    XXX
Summary:    Python library containting Mistral actions
License:    ASL 2.0
URL:        http://launchpad.net/mistral/

Source0:    http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%package -n python3-%{library}
Summary:    Python library containting Mistral actions
%{?python_provide:%python_provide python3-%{library}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-oslotest

BuildRequires:       python3-pbr >= 2.0.0
BuildRequires:       python3-babel >= 2.3.4
BuildRequires:       python3-oslo-log >= 3.36.0
BuildRequires:       python3-mistral-lib >= 2.3.0
BuildRequires:       python3-yaql >= 1.1.3
BuildRequires:       python3-oauthlib >= 0.6.2
BuildRequires:       python3-stestr >= 2.0.0

BuildRequires:       python3-aodhclient >= 0.9.0
BuildRequires:       python3-barbicanclient >= 4.5.2
BuildRequires:       python3-cinderclient >= 3.3.0
BuildRequires:       python3-designateclient >= 2.7.0
BuildRequires:       python3-glanceclient >= 1:2.8.0
BuildRequires:       python3-gnocchiclient >= 3.3.1
BuildRequires:       python3-heatclient >= 1.10.0
BuildRequires:       python3-ironic-inspector-client >= 1.5.0
BuildRequires:       python3-ironicclient >= 2.7.0
BuildRequires:       python3-keystoneauth1 >= 3.18.0
BuildRequires:       python3-keystoneclient >= 1:3.8.0
BuildRequires:       python3-magnumclient >= 2.15.0
BuildRequires:       python3-manilaclient >= 1.23.0
BuildRequires:       python3-mistralclient >= 3.1.0
BuildRequires:       python3-neutronclient >= 6.7.0
BuildRequires:       python3-novaclient >= 1:9.1.0
BuildRequires:       python3-swiftclient >= 3.2.0
BuildRequires:       python3-troveclient >= 2.2.0
BuildRequires:       python3-zaqarclient >= 1.0.0
%if 0%{rhosp} == 0
BuildRequires:       python3-muranoclient >= 1.3.0
BuildRequires:       python3-senlinclient >= 1.11.0
BuildRequires:       python3-tackerclient >= 0.8.0
BuildRequires:       python3-vitrageclient >= 2.0.0
%endif

Requires:       python3-pbr >= 2.0.0
Requires:       python3-babel >= 2.3.4
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-mistral-lib >= 2.3.0
Requires:       python3-yaql >= 1.1.3
Requires:       python3-oauthlib >= 0.6.2
Requires:       python3-aodhclient >= 0.9.0
Requires:       python3-barbicanclient >= 4.5.2
Requires:       python3-cinderclient >= 3.3.0
Requires:       python3-designateclient >= 2.7.0
Requires:       python3-glanceclient >= 1:2.8.0
Requires:       python3-gnocchiclient >= 3.3.1
Requires:       python3-heatclient >= 1.10.0
Requires:       python3-ironic-inspector-client >= 1.5.0
Requires:       python3-ironicclient >= 2.7.0
Requires:       python3-keystoneauth1 >= 3.18.0
Requires:       python3-keystoneclient >= 1:3.8.0
Requires:       python3-magnumclient >= 2.15.0
Requires:       python3-manilaclient >= 1.23.0
Requires:       python3-mistralclient >= 3.1.0
Requires:       python3-neutronclient >= 6.7.0
Requires:       python3-novaclient >= 1:9.1.0
Requires:       python3-swiftclient >= 3.2.0
Requires:       python3-troveclient >= 2.2.0
Requires:       python3-zaqarclient >= 1.0.0
%if 0%{rhosp} == 0
Requires:       python3-muranoclient >= 1.3.0
Requires:       python3-senlinclient >= 1.11.0
Requires:       python3-tackerclient >= 0.8.0
Requires:       python3-vitrageclient >= 2.0.0
%endif

%description -n python3-%{library}
%{common_desc}


%package -n python3-%{library}-tests
Summary:    Mistral extras library tests
%{?python_provide:%python_provide python3-%{library}-tests}
Requires:   python3-%{library} = %{version}-%{release}

Requires:       python3-oslotest
Requires:       python3-subunit
Requires:       python3-testrepository

%description -n python3-%{library}-tests
Mistral extras library tests.

This package contains the Mistral extras library test files.

%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    Mistral extras library documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description -n python-%{library}-doc
Mistral extras library documentation

This package contains the documentation.
%endif

%description
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{library}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
# excluding one test due to upstream bug related to barbicanclient
stestr-3 run --exclude-regex 'mistral_extra.tests.unit.actions.openstack.test_generator.GeneratorTest.test_generator'

%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
