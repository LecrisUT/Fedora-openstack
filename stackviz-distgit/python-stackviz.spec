%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global pname stackviz

%global common_desc \
A visualization utility to help analyze the performance of \
DevStack setup and Tempest executions

Name:           python-%{pname}
Version:        XXX
Release:        XXX
Summary:        Visualization utility

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{pname}
Source0:        http://tarballs.openstack.org/%{name}/%{pname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{name}/%{pname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  python3-subunit
BuildRequires:  python3-docutils
BuildRequires:  python3-oslo-db
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  openstack-macros

# Test requirements

BuildRequires:  python3-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-openstackdocstheme

%description
%{common_desc}

%package -n     python3-%{pname}
Summary:        Tempest visualization utility
%{?python_provide:%python_provide python3-%{pname}}

Requires:       python3-oslo-db >= 6.0.0
Requires:       python3-six
Requires:       python3-subunit
Requires:       python3-stestr
Requires:       python3-testrepository
Requires:       python3-testtools

%description -n python3-%{pname}
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n stackviz-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}

%install

%{py3_install}

%check
export PYTHON=%{__python3}
stestr run

%files -n python3-%{pname}
%license LICENSE
%doc README.rst
%{_bindir}/stackviz-export
%{python3_sitelib}/stackviz
%{python3_sitelib}/stackviz*.egg-info

%changelog
