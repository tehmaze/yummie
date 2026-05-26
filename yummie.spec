Name:           yummie
Version:        0.2.0
Release:        1%{?dist}
Summary:        Automated system upgrades using yum

License:        MIT
URL:            https://github.com/tehmaze/yummie
Vendor:         https://maze.io
Source0:        https://github.com/tehmaze/yummie/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

Requires:       python3
Requires:       yum


%description
Automated system upgrades using yum.


%prep
%autosetup

%build

%install
%make_install


%files
%doc README.md
%{_bindir}/yummie
%config(noreplace) %{_sysconfdir}/yum/yummie.conf

%changelog
* Sun May 24 2026 Jose Oliveira
- Specfile modernization
