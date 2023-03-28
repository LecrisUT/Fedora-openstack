%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    XXX
Release:    XXX
License:    ASL 2.0
Group:      System Environment/Base
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:    https://tarballs.openstack.org/dib-utils/dib-utils-%{upstream_version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

Conflicts: diskimage-builder < 0.1.15

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}


%files
%doc README.md
%{_bindir}/dib-run-parts
%{python3_sitelib}/dib_utils*

%changelog
