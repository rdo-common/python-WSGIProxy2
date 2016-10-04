# Created by pyp2rpm-1.1.0b
%global pypi_name WSGIProxy2
%global package_name wsgiproxy
%global with_python3 0

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        1%{?dist}
Summary:        WSGI Proxy that supports several HTTP backends

License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source0:        https://pypi.python.org/packages/source/W/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # if with_python3
 
Requires:       python-webob
Requires:       python-six

%description
WSGI Proxy that supports several HTTP backends.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        WSGI Proxy that supports several HTTP backends
 
Requires:       python3-webob
Requires:       python3-six

%description -n python3-%{pypi_name}
WSGI Proxy that supports several HTTP backends.
This package contains Python 3 build of the library.
%endif # with_python3


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc README_fixt.py README.rst
%{python2_sitelib}/%{package_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README_fixt.py README.rst
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif # with_python3


%changelog
* Thu Jun 05 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.1-1
- Initial package.
