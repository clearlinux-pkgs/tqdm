#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tqdm
Version  : 4.59.0
Release  : 97
URL      : https://files.pythonhosted.org/packages/ef/58/60cc1e9af5714d1b86062f6dc00c5dd6973c902da6259f930b9c6e7a3430/tqdm-4.59.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/58/60cc1e9af5714d1b86062f6dc00c5dd6973c902da6259f930b9c6e7a3430/tqdm-4.59.0.tar.gz
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin = %{version}-%{release}
Requires: tqdm-license = %{version}-%{release}
Requires: tqdm-python = %{version}-%{release}
Requires: tqdm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pycodestyle
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : toml-python

%description
tqdm
        ====
        
        |Py-Versions| |Versions| |Conda-Forge-Status| |Docker| |Snapcraft|
        
        |Build-Status| |Coverage-Status| |Branch-Coverage-Status| |Codacy-Grade| |Libraries-Rank| |PyPI-Downloads|
        
        |LICENCE| |OpenHub-Status| |binder-demo| |awesome-python|
        
        ``tqdm`` derives from the Arabic word *taqaddum* (تقدّم) which can mean "progress,"
        and is an abbreviation for "I love you so much" in Spanish (*te quiero demasiado*).
        
        Instantly make your loops show a smart progress meter - just wrap any
        iterable with ``tqdm(iterable)``, and you're done!

%package bin
Summary: bin components for the tqdm package.
Group: Binaries
Requires: tqdm-license = %{version}-%{release}

%description bin
bin components for the tqdm package.


%package license
Summary: license components for the tqdm package.
Group: Default

%description license
license components for the tqdm package.


%package python
Summary: python components for the tqdm package.
Group: Default
Requires: tqdm-python3 = %{version}-%{release}

%description python
python components for the tqdm package.


%package python3
Summary: python3 components for the tqdm package.
Group: Default
Requires: python3-core
Provides: pypi(tqdm)

%description python3
python3 components for the tqdm package.


%prep
%setup -q -n tqdm-4.59.0
cd %{_builddir}/tqdm-4.59.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615221463
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
mkdir -p %{buildroot}/usr/share/package-licenses/tqdm
cp %{_builddir}/tqdm-4.59.0/LICENCE %{buildroot}/usr/share/package-licenses/tqdm/b4d93a527c38de0e53b77ab0b5011b4cff72c285
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tqdm/b4d93a527c38de0e53b77ab0b5011b4cff72c285

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
