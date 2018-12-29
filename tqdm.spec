#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x986B408043AE090D (tqdm@caspersci.uk.to)
#
Name     : tqdm
Version  : 4.28.1
Release  : 39
URL      : https://files.pythonhosted.org/packages/b0/9b/0b2f9dd0e42da42e17c79883021b21cda31dd3216aa2538205ccdd10cc7a/tqdm-4.28.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/9b/0b2f9dd0e42da42e17c79883021b21cda31dd3216aa2538205ccdd10cc7a/tqdm-4.28.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/b0/9b/0b2f9dd0e42da42e17c79883021b21cda31dd3216aa2538205ccdd10cc7a/tqdm-4.28.1.tar.gz.asc
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin = %{version}-%{release}
Requires: tqdm-license = %{version}-%{release}
Requires: tqdm-python = %{version}-%{release}
Requires: tqdm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pycodestyle

%description
tqdm
        ====
        
        |PyPI-Status| |PyPI-Versions| |Conda-Forge-Status|
        
        |Build-Status| |Coverage-Status| |Branch-Coverage-Status| |Codacy-Grade|
        
        |DOI-URI| |LICENCE| |OpenHub-Status|
        
        
        ``tqdm`` means "progress" in Arabic (taqadum, ØªÙØ¯ÙÙ)
        and is an abbreviation for "I love you so much" in Spanish (te quiero demasiado).
        
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

%description python3
python3 components for the tqdm package.


%prep
%setup -q -n tqdm-4.28.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540151548
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tqdm
cp LICENCE %{buildroot}/usr/share/package-licenses/tqdm/LICENCE
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
/usr/share/package-licenses/tqdm/LICENCE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
