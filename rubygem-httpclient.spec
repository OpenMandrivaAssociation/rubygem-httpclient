%define oname httpclient

Summary:    Gives something like the functionality of libwww-perl (LWP) in Ruby
Name:       rubygem-%{oname}
Version:    2.1.5.2
Release:    %mkrel 1
Group:      Development/Ruby
License:    Ruby or GPLv2
URL:        http://dev.ctor.org/httpclient
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
gives something like the functionality of libwww-perl (LWP) in Ruby

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{ruby_gemdir}/gems/%{oname}-%{version}/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 2.1.5.2-1mdv2011.0
+ Revision: 584435
- import rubygem-httpclient

