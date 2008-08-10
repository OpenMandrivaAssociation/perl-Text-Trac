%define module   Text-Trac
%define version    0.13
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for formatting text with Trac Wiki Style
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Test::Base)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Text::Trac parses text with Trac WikiFormatting and convert it to html
format.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Text
