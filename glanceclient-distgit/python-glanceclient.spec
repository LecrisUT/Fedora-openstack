%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname glanceclient
%global with_doc 1

%global common_desc \
This is a client for the OpenStack Glance API. There's a Python API (the \
glanceclient module), and a command-line script (glance). Each implements \
100% of the OpenStack Glance API.

Name:             python-glanceclient
Epoch:            1
Version:          XXX
Release:          XXX
Summary:          Python API and CLI for OpenStack Glance

License:          ASL 2.0
URL:              https://launchpad.net/python-glanceclient
Source0:          https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:        noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:    git-core
BuildRequires:    openstack-macros

%description
%{common_desc}

%package -n python3-%{sname}
Summary:          Python API and CLI for OpenStack Glance
%{?python_provide:%python_provide python3-glanceclient}
Obsoletes: python2-%{sname} < %{version}-%{release}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-pbr

Requires:         python3-keystoneauth1 >= 3.6.2
Requires:         python3-oslo-i18n >= 3.15.3
Requires:         python3-oslo-utils >= 3.33.0
Requires:         python3-pbr
Requires:         python3-prettytable
Requires:         python3-pyOpenSSL >= 17.1.0
Requires:         python3-requests
Requires:         python3-warlock
Requires:         python3-wrapt


%description -n python3-%{sname}
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:          Documentation for OpenStack Glance API Client

BuildRequires:    python3-sphinx
BuildRequires:    python3-openstackdocstheme
BuildRequires:    python3-keystoneauth1
BuildRequires:    python3-oslo-utils
BuildRequires:    python3-prettytable
BuildRequires:    python3-pyOpenSSL >= 17.1.0
BuildRequires:    python3-sphinxcontrib-apidoc
BuildRequires:    python3-warlock

%description      doc
%{common_desc}

This package contains auto-generated documentation.
%endif

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{name}-%{upstream_version} -S git

%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s glance %{buildroot}%{_bindir}/glance-3

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm 644 tools/glance.bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/glance

# Delete tests
rm -fr %{buildroot}%{python3_sitelib}/glanceclient/tests

%if 0%{?with_doc}
# generate html docs
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
# generate man page
sphinx-build -b man doc/source doc/build/man
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1
%endif

%files -n python3-%{sname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/glanceclient
%{python3_sitelib}/*.egg-info
%{_sysconfdir}/bash_completion.d
%if 0%{?with_doc}
%{_mandir}/man1/glance.1.gz
%endif
%{_bindir}/glance
%{_bindir}/glance-3

%if 0%{?with_doc}
%files doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
