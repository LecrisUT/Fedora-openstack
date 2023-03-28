%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
# Created by pyp2rpm-1.0.1
%global sname pycadf

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc DMTF Cloud Audit (CADF) data model


Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        DMTF Cloud Audit (CADF) data model

License:        ASL 2.0
URL:            https://launchpad.net/pycadf
Source0:        https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz.asc
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
Summary:        DMTF Cloud Audit (CADF) data model
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-pytz
Requires:       python3-six >= 1.10.0
Requires:       python-%{sname}-common = %{version}-%{release}

%description -n python3-%{sname}
%{common_desc}

%package -n python-%{sname}-common
Summary:        DMTF Cloud Audit (CADF) data model
%{?python_provide:%python_provide python-%{sname}-common}

%description -n python-%{sname}-common
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{sname}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{sname}.egg-info


%build
%{py3_build}


%install
%{py3_install}

mkdir -p %{buildroot}/%{_sysconfdir}
mv %{buildroot}/usr/etc/%{sname} %{buildroot}/%{_sysconfdir}/


%files -n python3-%{sname}
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-%{upstream_version}-py%{python3_version}.egg-info

%files -n python-%{sname}-common
%doc README.rst
%license LICENSE
%dir %{_sysconfdir}/%{sname}
%config(noreplace) %{_sysconfdir}/%{sname}/*.conf


%changelog
