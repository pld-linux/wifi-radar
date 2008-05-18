# TODO:
# - config should be accesible with some better rights...
Summary:	Utility for managing WiFi profiles
Summary(pl.UTF-8):	Narzędzie do zarządzania profilami WiFi
Name:		wifi-radar
Version:	1.9.9
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://wifi-radar.systemimager.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	fdcf862da67e0624dcca5d71d12caddf
Source1:	%{name}.conf
Source2:	%{name}.desktop
Source3:	%{name}-128.png
Patch0:		%{name}-path.diff
URL:		http://www.bitbuilder.com/wifi_radar/
Requires:	dhcpcd
Requires:	net-tools
Requires:	python-pygtk-gtk >= 2.4.0
Requires:	python-pycairo >= 1.2.2
Requires:	wireless-tools
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
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man{1,5}}

install wifi-radar wifi-radar.sh $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install pixmaps/wifi{-radar.*g,_radar_32x32.png} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE.LOG CREDITS README README.WPA-Mini-HOWTO.txt TODO
%attr(755,root,root) %{_sbindir}/*
# rights should be changed? taken from SuSE
%attr(600,root,root) %config(noreplace) %{_sysconfdir}/wifi-radar.conf
%{_desktopdir}/wifi-radar.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.svg
%{_mandir}/man1/*
%{_mandir}/man5/*
