%global pypi_name collectd-gnocchi
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Gnocchi storage plugin for collectd

License:        ASL 2.0
URL:            https://github.com/gnocchixyz/collectd-gnocchi
Source0:        https://github.com/gnocchixyz/collectd-gnocchi/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
BuildRequires:  git-core
Requires:       collectd-python

%description
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%package -n     python3-%{pypi_name}
Summary:        Gnocchi storage plugin for collectd
%{?python_provide:%python_provide python3-%{pypi_name}}
Obsoletes: python2-%{pypi_name} < %{version}-%{release}

Requires:       python3-gnocchiclient >= 4.0.0
Requires:       python3-keystoneauth1 >= 3.3.0
%description -n python3-%{pypi_name}
 collectdgnocchi This is an output plugin for collectd_ that send metrics to
Gnocchi_. It will create a resource type named _collectd_ (by default) and a
new resource for each of the host monitored.Each host will have a list of
metrics created dynamically using the following name convention:
pluginplugin_instance/typetype_instancevalue_numberIn order for the metric to
be created correctly, be ...

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{py3_build}

%install
%{py3_install}


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/collectd_gnocchi
%{python3_sitelib}/collectd_gnocchi-*-py*.egg-info

%changelog
