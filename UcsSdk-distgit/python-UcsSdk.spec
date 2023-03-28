%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global package_name UcsSdk

Name:           python-%{package_name}
Version:        XXX
Release:        XXX
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.io/packages/source/U/UcsSdk/UcsSdk-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%{python2_sitelib}/%{package_name}/
%{python2_sitelib}/%{package_name}*.egg-info
%doc README.md
%license LICENSE.txt

%changelog
