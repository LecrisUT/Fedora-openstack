%global pypi_name openstacksdk
%global srcname %{pypi_name}


Name:           python-openstacksdk
Version:        1.0.1
Release:        %{autorelease}
Summary:        An SDK for building applications to work with OpenStack

License:        ASL 2.0
URL:            http://www.openstack.org/openstack/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  git-core

%global common_desc \
A collection of libraries for building applications to work with OpenStack \
clouds.

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        An SDK for building applications to work with OpenStack

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%autosetup -n %{srcname}-%{version} -S git
%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install
%pyproject_save_files openstack

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/openstack-inventory
%exclude %{python3_sitelib}/openstack/tests

%changelog
%autochangelog
