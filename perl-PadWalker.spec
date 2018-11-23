#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PadWalker
Version  : 2.3
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/R/RO/ROBIN/PadWalker-2.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RO/ROBIN/PadWalker-2.3.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpadwalker-perl/libpadwalker-perl_2.3-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-PadWalker-lib = %{version}-%{release}
Requires: perl-PadWalker-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
-----------------------------------------------------------------------------
| PadWalker v2.3    - Robin Houston
-----------------------------------------------------------------------------

%package dev
Summary: dev components for the perl-PadWalker package.
Group: Development
Requires: perl-PadWalker-lib = %{version}-%{release}
Provides: perl-PadWalker-devel = %{version}-%{release}

%description dev
dev components for the perl-PadWalker package.


%package lib
Summary: lib components for the perl-PadWalker package.
Group: Libraries
Requires: perl-PadWalker-license = %{version}-%{release}

%description lib
lib components for the perl-PadWalker package.


%package license
Summary: license components for the perl-PadWalker package.
Group: Default

%description license
license components for the perl-PadWalker package.


%prep
%setup -q -n PadWalker-2.3
cd ..
%setup -q -T -D -n PadWalker-2.3 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/PadWalker-2.3/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PadWalker
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-PadWalker/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/PadWalker.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PadWalker.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/PadWalker/PadWalker.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PadWalker/deblicense_copyright
