#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yamlloader
Version  : 0.5.5
Release  : 6
URL      : https://files.pythonhosted.org/packages/d5/93/11628e0d09213b7570d625b3399045f0eb413bbe49a400d764d1d612d807/yamlloader-0.5.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/93/11628e0d09213b7570d625b3399045f0eb413bbe49a400d764d1d612d807/yamlloader-0.5.5.tar.gz
Summary  : Ordered YAML loader and dumper for PyYAML.
Group    : Development/Tools
License  : MIT
Requires: yamlloader-python = %{version}-%{release}
Requires: yamlloader-python3 = %{version}-%{release}
Requires: PyYAML
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3

%description
.. image:: https://travis-ci.org/Phynix/yamlloader.svg?branch=master
:target: https://travis-ci.org/Phynix/yamlloader
.. image:: https://img.shields.io/pypi/pyversions/yamlloader.svg
:target: https://pypi.org/project/yamlloader/
.. image:: https://landscape.io/github/Phynix/yamlloader/master/landscape.svg?style=flat
:target: https://landscape.io/github/Phynix/yamlloader/master
:alt: Code Health
.. image:: https://www.versioneye.com/user/projects/5a2f00060fb24f07e40988bf/badge.svg?style=flat-square
:target: https://www.versioneye.com/user/projects/5a2f00060fb24f07e40988bf
:alt: Dependency Status
.. image:: https://coveralls.io/repos/github/Phynix/yamlloader/badge.svg
:target: https://coveralls.io/github/Phynix/yamlloader

%package python
Summary: python components for the yamlloader package.
Group: Default
Requires: yamlloader-python3 = %{version}-%{release}

%description python
python components for the yamlloader package.


%package python3
Summary: python3 components for the yamlloader package.
Group: Default
Requires: python3-core
Provides: pypi(yamlloader)
Requires: pypi(pyyaml)

%description python3
python3 components for the yamlloader package.


%prep
%setup -q -n yamlloader-0.5.5
cd %{_builddir}/yamlloader-0.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597083628
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
