%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:0}%{?_without_doc:1}

%global sname os-faults
%global pypi_name os_faults

%{?dlrn: %global tarsources %{pypi_name}-%{upstream_version}}
%{!?dlrn: %global tarsources %{sname}}

%global common_desc \
OSFaults **OpenStack faultinjection library**The library does destructive \
actions inside an OpenStack cloud. It provides an abstraction layer over \
different types of cloud deployments. The actions are implemented as drivers \
(e.g. DevStack driver, Libvirt driver, IPMI driver).

Name:           python-%{sname}
Version:        XXX
Release:        XXX
Summary:        OpenStack fault-injection library

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/%{sname}
Source0:        https://opendev.org/performa/%{sname}/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
# Test requirements
BuildRequires:  python3-pytest
BuildRequires:  python3-ddt
BuildRequires:  python3-mock
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-pyghmi
BuildRequires:  python3-appdirs
BuildRequires:  python3-jsonschema
BuildRequires:  python3-oslo-concurrency
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-i18n
BuildRequires:  openstack-macros
BuildRequires:  /usr/bin/which

BuildRequires:  python3-libvirt
BuildRequires:  python3-PyYAML
BuildRequires: (python3dist(ansible) or ansible-core >= 2.11)
BuildRequires:  python3-click
BuildRequires:  /usr/bin/pathfix.py

%description
%{common_desc}

%package -n     python3-%{sname}
Summary:        OpenStack fault-injection library
%{?python_provide:%python_provide python3-%{sname}}
Obsoletes: python2-%{sname} < %{version}-%{release}

Requires:       python3-pbr >= 2.0.0
Requires:       python3-appdirs >= 1.3.0
Requires:       python3-jsonschema >= 2.6.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-oslo-concurrency >= 3.0.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-utils >= 3.20.0
Requires:       python3-pyghmi
Requires:       python3-six >= 1.9.0
Requires:       /usr/bin/which

Requires:       (python3dist(ansible) >= 2.2 or ansible-core >= 2.11)
Requires:       python3-click
Requires:       python3-yaml >= 3.10.0

%description -n python3-%{sname}
%{common_desc}

%package -n     python3-%{sname}-libvirt
Summary:        OpenStack fault-injection library libvirt plugin
%{?python_provide:%python_provide python3-%{sname}-libvirt}

Requires:       python3-%{sname} = %{version}-%{release}

Requires:       python3-libvirt


%description -n python3-%{sname}-libvirt
%{common_desc}

It contains libvirt plugin for OpenStack faultinjection library.

%package -n      python3-%{sname}-tests
Summary:         OpenStack fault-injection library
%{?python_provide:%python_provide python3-%{sname}-tests}
Requires:        python3-%{sname} = %{version}-%{release}

Requires:        python3-pytest
Requires:        python3-ddt
Requires:        python3-mock
Requires:        python3-subunit
Requires:        python3-oslotest
Requires:        python3-testrepository
Requires:        python3-testscenarios
Requires:        python3-testtools
Requires:        python3-appdirs

%description -n  python3-%{sname}-tests
%{common_desc}

It contains unittests for OpenStack faultinjection library.

%if 0%{?with_doc}
%package -n python-%{sname}-doc
Summary:        os_faults documentation

BuildRequires:    python3-sphinx
BuildRequires:    python3-appdirs
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-oslo-serialization
BuildRequires:    python3-oslo-i18n
BuildRequires:    python3-jsonschema
BuildRequires:    python3-sphinx_rtd_theme

BuildRequires:    python3-PyYAML
BuildRequires:    python3-click
BuildRequires: (python3dist(ansible) or ansible-core >= 2.11)

%description -n python-%{sname}-doc
%{common_desc}

It contains the documentation for OpenStack faultinjection library.
%endif

%prep
%autosetup -n %{tarsources} -S git
%py_req_cleanup

# The test relies on binary 'ansible-playbook' but ansible-python3
# in Fedora doesn't provide it, so need to hack test file.
sed -i 's/ansible-playbook/ansible-playbook-3/' os_faults/ansible/executor.py

# sphinxcontrib-programoutput is required by os-faults while building
# sphinx doc theme. sphinxcontrib-programoutput is dependent on js-query
# while js-query starts pulling lots of node.js dependency.
# So, removing sphinxcontrib-programoutput dependency.

sed -i '/sphinxcontrib.programoutput/d' doc/source/conf.py
sed -i '/sphinx.ext.autosectionlabel/d' doc/source/conf.py

%build
%{py3_build}

%if 0%{?with_doc}
%{__python3} setup.py build_sphinx
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%install
FAULT_EXEC="os-inject-fault os-faults"
%{py3_install}
for binary in $FAULT_EXEC; do
  # Create a versioned binary for backwards compatibility until everything is pure py3
  ln -s ${binary} %{buildroot}%{_bindir}/${binary}-3
done
# Make executables
for file in %{buildroot}%{python3_sitelib}/%{pypi_name}/ansible/modules/{freeze,kill}.py; do
   chmod a+x $file
      # Fix shebangs for Python 3-only distros
      pathfix.py -pni "%{__python3} %{py3_shbang_opts}" $file
done

%check
py.test-3 -vvvv --durations=10 "os_faults/tests/unit"

%files -n python3-%{sname}
%license LICENSE
%doc README.rst
%{_bindir}/os-inject-fault
%{_bindir}/os-inject-fault-3
%{_bindir}/os-faults
%{_bindir}/os-faults-3
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests
%exclude %{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python3-%{sname}-libvirt
%license LICENSE
%{python3_sitelib}/%{pypi_name}/drivers/power/libvirt.py*

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_doc}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
