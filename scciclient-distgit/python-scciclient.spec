%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global src_name scciclient
%global pkg_name python-scciclient
%global sum Python ServerView Common Command Interface (SCCI) Client Library

%global common_desc \
Python ServerView Common Command Interface (SCCI) Client Library

Name:        %{pkg_name}
Version:     XXX
Release:     XXX
Summary:     %{sum}
License:     ASL 2.0
URL:         https://pypi.python.org/pypi/%{pkg_name}
Source0:     https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pkg_name}/%{pkg_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:   noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}


%package -n python3-%{src_name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{src_name}}

BuildRequires: python3-devel
BuildRequires: python3-pbr
BuildRequires: python3-setuptools
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslo-sphinx
BuildRequires: python3-testscenarios
BuildRequires: python3-stestr
BuildRequires: python3-mock
BuildRequires: python3-pyghmi
BuildRequires: python3-pysnmp
BuildRequires: python3-oslo-serialization
BuildRequires: python3-defusedxml
BuildRequires: git-core

BuildRequires: python3-requests-mock

Requires: python3-pbr >= 2.0.0
Requires: python3-babel >= 2.3.4
Requires: python3-requests >= 2.14.2
Requires: python3-six >= 1.10.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-pyghmi >= 1.0.24
Requires: python3-pysnmp >= 4.2.3
Requires: python3-defusedxml >= 0.7.0

%description -n python3-%{src_name}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pkg_name}-%{upstream_version} -S git

%build
%{py3_build}

%install
%{py3_install}

%check
PYTHON=%{__python3} stestr run

%files -n python3-%{src_name}
%license LICENSE
%doc README.rst
%doc AUTHORS
%{python3_sitelib}/%{src_name}
%{python3_sitelib}/*.egg-info

%changelog
