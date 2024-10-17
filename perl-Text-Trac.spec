%define upstream_name    Text-Trac
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for formatting text with Trac Wiki Style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Base)
BuildRequires:	perl(Tie::IxHash)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html
format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Text

%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 664900
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 405716
- rebuild using %%perl_convert_version

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2009.1
+ Revision: 353670
- update to new version 0.15

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 344389
- update to new version 0.14

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2009.0
+ Revision: 270399
- update to new version 0.13

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.12-2mdv2009.0
+ Revision: 268839
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.0
+ Revision: 194956
- update to new version 0.12

* Thu Mar 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.1
+ Revision: 180578
- update to new version 0.11

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 178278
- update to new version 0.10
- update to new version 0.10

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.1
+ Revision: 177897
- import perl-Text-Trac


