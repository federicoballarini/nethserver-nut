Summary: NethServer NUT configuration
Name: nethserver-nut
Version: 1.5.2
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-cockpit.tar.gz
BuildArch: noarch

Requires: nethserver-base
Requires: nut

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
NethServer UPS management using NUT

%prep
%setup

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

%{genfilelist} %{buildroot}  --file /etc/sudoers.d/50_nsapi_nethserver_nut 'attr(0440,root,root)' > %{name}-%{version}-filelist

cat %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
%ghost %attr(0644, root, root) %{_sysconfdir}/collectd.d/nut_nethserver.conf

%changelog
* Mon Oct 28 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.5.2-1
- Logs page in Cockpit - Bug NethServer/dev#5866

* Thu Oct 10 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.5.1-1
- Cockpit: improve English labels - NethServer/dev#5856

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.5.0-1
- Sudoers based authorizations for Cockpit UI - NethServer/dev#5805

* Tue Sep 03 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.1-1
- Cockpit. List correct application version - Nethserver/dev#5819

* Wed Jun 12 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.4.0-1
- Nut Cockpit UI - NethServer/dev#5772

* Thu Aug 09 2018 Davide Principi <davide.principi@nethesis.it> - 1.3.2-1
- Enhancement: (un)mask password fields - NethServer/dev#5554

* Tue May 16 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.1-1
- NUT UPS master unreachable from clients - Bug NethServer/dev#5282

* Thu Jul 21 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.3.0-1
- collectd - monitor only locally connected ups - NethServer/dev#5049

* Fri Jul 08 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.1-1
- Fix .spec typo

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.0-1
- First NS7 release

* Fri May 27 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.12-1
- Dashboard/UPS: no info for some UPS models - Enhancement #3397 [NethServer]

* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.11-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]
- nethserver-devbox replacements - Feature #3009 [NethServer]

* Wed Oct 15 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.10-1.ns6
- Fix dashboard error when configured as slave - Bug #2842

* Tue Jul 08 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.8-1.ns6
- Fix web interface: device not saved - Bug #2800

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.7-1.ns6
- Revamp web UI style - Enhancement #2656 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.6-1.ns6
- Move admin user in LDAP DB - Feature #2492 [NethServer]
- NUT: add option to enable mail notification - Enhancement #2291 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Wed Oct 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.5-1.ns6
- Upsd daemon should listen on 0.0.0.0 - Enhancement #2139
- Db defaults: remove Runlevels prop. Refs #2067

* Tue Jul 23 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1.ns6
- Auto-generate password on first install #1760
- Added a simple form for driver suggestion during UPS configuration #1760

* Tue Jul 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Bump release #1760 [NethServer]

* Tue Jul 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- web ui: remove php warning on temperature parameter. #1760

* Tue Jul 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Fix warnings on Dashboard when no UPS is connected #1760
- Fix upsd.conf template

* Fri Jun 07 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release
