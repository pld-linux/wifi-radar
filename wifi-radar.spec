# TODO:
# - config should be accesible with some better rights...
# NOTE:
# - there is some GNOME/PAM integration described at http://wifi-radar.systemimager.org/
# - there are %{name}.{conf,desktop} files in tarball too
# - Consider using default .desktop
Summary:	Utility for managing WiFi profiles
Summary(pl.UTF-8):	Narzędzie do zarządzania profilami WiFi
Name:		wifi-radar
Version:	2.0.s07
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	http://download.berlios.de/wifi-radar/%{name}-%{version}.tar.bz2
# Source0-md5:	f68e0f63fd3b03cd4b669f1c06734303
Source1:	%{name}.conf
Source2:	%{name}.desktop
Source3:	%{name}-128.png
URL:		http://wifi-radar.systemimager.org/
Requires:	dhcpcd
Requires:	net-tools
Requires:	python-pycairo >= 1.2.2
Requires:	python-pygtk-gtk >= 2.4.0
Requires:	wireless-tools
Suggests:	sudo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WiFi Radar is a Python/PyGTK2 utility for managing WiFi profiles. It
enables you to scan for available networks and create profiles for
your preferred networks. At boot time, running WiFi Radar will
automatically scan for an available preferred network and connect to
it. You can drag and drop your preferred networks to arrange the
profile priority.

%description -l pl.UTF-8
WiFi Radar to narzędzie do zarządzania profilami połączeń WiFi
napisane przy użyciu Pythona/PyGTK2. Umożliwia skanowanie w
poszukiwaniu dostępnych sieci i tworzenie dla nich profili. Podczas
uruchamiania komputera WiFi Radar automatycznie przeskanuje w
poszukiwaniu preferowanej sieci i połączy się z nią. Można użyć
przeciągania aby zorganizować priorytety profili.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_sysconfdir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man{1,5}}

install wifi-radar $RPM_BUILD_ROOT%{_sbindir}
install wifi-radar.sh $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install pixmaps/wifi{-radar.*g,_radar_32x32.png} $RPM_BUILD_ROOT%{_pixmapsdir}
install man/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man5/%{name}.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_sbindir}/wifi-radar
%attr(755,root,root) %{_bindir}/wifi-radar.sh
# rights should be changed? taken from SuSE
%attr(600,root,root) %config(noreplace) %{_sysconfdir}/wifi-radar.conf
%{_desktopdir}/wifi-radar.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.svg
%{_mandir}/man1/wifi-radar.1*
%{_mandir}/man5/wifi-radar.conf.5*
