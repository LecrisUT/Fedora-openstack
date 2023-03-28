%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global with_doc 1
%global sname sushy-tools
%global fname sushy_tools
%global common_desc A set of tools to support the development and test of the Sushy library
%global common_desc_tests Tests for sushy-tools library

Name: python-%{sname}
Version: XXX
Release: XXX
Summary: %{common_desc}
License: ASL 2.0
URL: https://opendev.org/openstack/sushy-tools

Source0: https://tarballs.opendev.org/openstack/%{sname}/%{sname}-%{upstream_version}.tar.gz
Source1: sushy-emulator.service
Source2: sushy-emulator.conf
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101: http://tarballs.openstack.org/%{sname}/%{sname}-%{upstream_version}.tar.gz.asc
Source102: https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildRequires: git-core
BuildArch: noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
%{common_desc}

%package -n python3-%{sname}
Summary: %{common_desc}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
BuildRequires: python3-flask
BuildRequires: python3-ironic-lib
BuildRequires: python3-pbr
BuildRequires: python3-requests
BuildRequires: python3-setuptools
BuildRequires: python3-tenacity

Requires: python3-flask >= 1:1.0.2
Requires: python3-ironic-lib >= 4.6.1
Requires: python3-requests >= 2.14.2
Requires: python3-tenacity >= 6.2.0

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: sushy-tools tests
Requires: python3-%{sname} = %{version}-%{release}

BuildRequires: python3-libvirt
BuildRequires: python3-munch
BuildRequires: python3-openstacksdk
BuildRequires: python3-oslotest
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires: python3-libvirt
Requires: python3-munch
Requires: python3-openstacksdk
Requires: python3-oslotest
Requires: python3-testscenarios
Requires: python3-testtools

%description -n python3-%{sname}-tests
%{common_desc_tests}

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary: sushy-tools documentation

BuildRequires: python3-sphinx
BuildRequires: python3-sphinxcontrib-apidoc
BuildRequires: python3-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for sushy-tools
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
sphinx-build-3 -W -b html doc/source doc/build/html
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}
# Install systemd script
mkdir -p %{buildroot}%{_unitdir}
install -p -D -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/sushy-emulator.service
# Install distribution config
mkdir -p %{buildroot}%{_sysconfdir}/sushy-emulator/
install -p -D -m 640 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sushy-emulator/sushy-emulator.conf

%check
%{__python3} setup.py test

%pre -n python3-%{sname}
getent group sushy-tools >/dev/null || groupadd -r sushy-tools
getent passwd sushy-tools >/dev/null || useradd -r \
    -g sushy-tools -M -s /sbin/nologin -c "Redfish Emulator" sushy-tools

%preun -n python3-%{sname}
%systemd_preun sushy-emulator.service

%post -n python3-%{sname}
%systemd_post sushy-emulator.service

%postun -n python3-%{sname}
%systemd_postun_with_restart sushy-emulator.service

%files -n python3-%{sname}
%license LICENSE
%{_bindir}/sushy-emulator
%{_bindir}/sushy-static
%{python3_sitelib}/%{fname}
%{python3_sitelib}/%{fname}-*.egg-info
%{_unitdir}/sushy-emulator.service
%dir %attr(-, root, sushy-tools) %{_sysconfdir}/sushy-emulator
%config(noreplace) %attr(-, root, sushy-tools) %{_sysconfdir}/sushy-emulator/sushy-emulator.conf
%exclude %{python3_sitelib}/%{dname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{fname}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
