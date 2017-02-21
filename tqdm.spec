#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x215746F12B131B20 (casper.dcl@physics.org)
#
Name     : tqdm
Version  : 4.11.2
Release  : 2
URL      : https://pypi.python.org/packages/46/b0/615b394ac0b25f1f1ef229e223c335558d69db97301c93e932fb7e5e4679/tqdm-4.11.2.tar.gz
Source0  : https://pypi.python.org/packages/46/b0/615b394ac0b25f1f1ef229e223c335558d69db97301c93e932fb7e5e4679/tqdm-4.11.2.tar.gz
Source99 : https://pypi.python.org/packages/46/b0/615b394ac0b25f1f1ef229e223c335558d69db97301c93e932fb7e5e4679/tqdm-4.11.2.tar.gz.asc
Summary  : Fast, Extensible Progress Meter
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: tqdm-bin
Requires: tqdm-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pycodestyle
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
|Logo|
tqdm
====
|PyPI-Status| |PyPI-Versions| |Conda-Forge-Status|
|Build-Status| |Coverage-Status| |Branch-Coverage-Status| |Codacy-Grade|

%package bin
Summary: bin components for the tqdm package.
Group: Binaries

%description bin
bin components for the tqdm package.


%package python
Summary: python components for the tqdm package.
Group: Default

%description python
python components for the tqdm package.


%prep
%setup -q -n tqdm-4.11.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487699912
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487699912
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tqdm

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
