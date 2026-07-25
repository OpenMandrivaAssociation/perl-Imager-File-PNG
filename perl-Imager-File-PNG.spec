%define upstream_name    Imager-File-PNG
%define upstream_version 1.002

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    Check that a library is available
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/tonycoz/imager
Source0:    https://cpan.metacpan.org/authors/id/T/TO/TONYC/Imager-File-PNG-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires: perl(Imager)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Imager's PNG support is documented in the Imager::Files manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


