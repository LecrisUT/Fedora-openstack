%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
# %global sources_gpg_sign <get the Cryptographic Signatures of current release from https://releases.openstack.org/#cryptographic-signatures>
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%global srcname ansible_role_collect_logs
%global rolename ansible-role-collect-logs

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role to collect the logs from a TripleO/OSP based deployment of OpenStack

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-collect-logs
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires: (python3dist(ansible) or ansible-core >= 2.11)
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  /usr/bin/pathfix.py

Requires: (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible role to collect the logs from a TripleO/OSP based deployment of OpenStack

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{rolename}-%{upstream_version} -S git
#Remove ansible from requirements.txt as dependency on ansible is managed manually
sed -i '/^ansible/d' requirements.txt


%build
%py3_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install
# Fix shebang
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}/usr/share/ansible/roles/collect-logs/library/flatten_nested_dict.py

%check
ROLE_NAME="collect-logs"
ansible-galaxy list -p %{buildroot}/usr/share/ansible/roles $ROLE_NAME|grep -v "$ROLE_NAME was not found"

%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
