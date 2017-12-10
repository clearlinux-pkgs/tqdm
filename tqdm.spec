#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x986B408043AE090D (tqdm@caspersci.uk.to)
#
Name     : tqdm
Version  : 4.19.5
Release  : 14
URL      : https://pypi.python.org/packages/19/c6/4d74a16323f5045e6d4444bd1e3104b8ba52507700bc152a9c6bd88d1cfb/tqdm-4.19.5.tar.gz
Source0  : https://pypi.python.org/packages/19/c6/4d74a16323f5045e6d4444bd1e3104b8ba52507700bc152a9c6bd88d1cfb/tqdm-4.19.5.tar.gz
Source99 : https://pypi.python.org/packages/19/c6/4d74a16323f5045e6d4444bd1e3104b8ba52507700bc152a9c6bd88d1cfb/tqdm-4.19.5.tar.gz.asc
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin
Requires: tqdm-python3
Requires: tqdm-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycodestyle
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
tqdm
        ====
        
        |PyPI-Status| |PyPI-Versions| |Conda-Forge-Status|
        
        |Build-Status| |Coverage-Status| |Branch-Coverage-Status| |Codacy-Grade|
        
        |DOI-URI| |LICENCE| |OpenHub-Status|
        
        
        ``tqdm`` means "progress" in Arabic (taqadum, ØªÙØ¯ÙÙ)
        and an abbreviation for "I love you so much" in Spanish (te quiero demasiado).
        
        Instantly make your loops show a smart progress meter - just wrap any
        iterable with ``tqdm(iterable)``, and you're done!

%package bin
Summary: bin components for the tqdm package.
Group: Binaries

%description bin
bin components for the tqdm package.


%package python
Summary: python components for the tqdm package.
Group: Default
Requires: tqdm-python3

%description python
python components for the tqdm package.


%package python3
Summary: python3 components for the tqdm package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tqdm package.


%prep
%setup -q -n tqdm-4.19.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512941879
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)
/usr/man/man1/tqdm.1

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
