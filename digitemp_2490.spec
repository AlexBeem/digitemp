Summary: DigiTemp, a one-wire LAN temperature sensor reader
Name: digitemp
Version: 3.5.0
Release: 1_ds2490
Copyright: GPL
Group: Applications/System
Source: http://www.digitemp.com/software/linux/digitemp-3.5.0.tar.gz
URL: http://www.digitemp.com
Packager: bcl@brianlane.com
Prefix: /usr/local
Buildroot: /var/tmp/%{name}-buildroot

%description
DigiTemp is a console application for reading Dallas Semiconductor 1-wire
network temperature sensors. It supports the DS18S20, DS18B20, DS1822.
This version requires a DS2490 USB to 1-wire adapter.

It includes perl scripts for logging using RRDB and MySQL, as well as a 
NetSaint/Nagios plugin and graph generating scripts using RRDB.

Release 3.x.x introduces compile time support for DS9097 passive adapters.
Version 3.3.0 introduces support for DS2438 battery monitor, and AAG TAI-8540
humidity sensor module.

This RPM package has been compiled for the DS2490 1-wire adapter.

NOTE: You need to be root to run the ds2490 version.

%prep
%setup

%build
make ds2490

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/local/bin/
install -s -g lock -m 2755 digitemp_DS2490 $RPM_BUILD_ROOT/usr/local/bin/
install -d -m 755 $RPM_BUILD_ROOT/usr/local/man/man1/
install -s -m 644 digitemp.1 $RPM_BUILD_ROOT/usr/local/man/man1/

%files
%doc COPYRIGHT COPYING FAQ README ChangeLog CREDITS
/usr/local/man/man1/digitemp.1
/usr/local/bin/digitemp_DS2490
