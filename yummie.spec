Name:           yummie
Version:        0.0.1
Release:        1%{?dist}
Summary:        Automated system upgrades using yum

Group:          System Environment/Base
License:        MIT
URL:            https://github.com/tehmaze/yummie
Vendor:         https://maze.io
Source0:        yummie
Source1:        yummie.conf.example

Requires:       python, yum


%description
Automated system upgrades using yum.

%prep

%build

%install
if [ "${RPM_BUILD_ROOT}" != "/" ]; then
    rm -rf "${RPM_BUILD_ROOT}"
fi

make install DESTDIR="${RPM_BUILD_ROOT}"

%clean
if [ "${RPM_BUILD_ROOT}" != "/" ]; then
    rm -rf "${RPM_BUILD_ROOT}"
fi

%files
%defattr(-, root, root, -)
%doc README.md
/usr/bin/yummie
%config(noreplace)/etc/yum/yummie.conf

%changelog
* Mon Jan 28 2013 Wijnand Modderman-Lenstra <maze@pyth0n.org> - 0.0.1-1
- initial version
