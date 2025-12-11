#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Notification daemon for LXQt desktop suite
Summary(pl.UTF-8):	Demon powiadomień dla środowiska graficznego LXQt
Name:		lxqt-notificationd
Version:	2.3.1
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-notificationd/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	98dc4ca92f2773fdbf1b894fb988274b
URL:		http://www.lxqt.org/
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kf6-kwindowsystem-devel >= 6.0.0
BuildRequires:	kp6-layer-shell-qt-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Notification daemon for LXQt desktop suite.

%description -l pl.UTF-8
Demon powiadomień dla środowiska graficznego LXQt.

%prep
%setup -q

%build
%cmake  -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-notificationd
%attr(755,root,root) %{_bindir}/lxqt-notificationd
/etc/xdg/autostart/lxqt-notifications.desktop
%{_desktopdir}/lxqt-config-notificationd.desktop
# needed for the lang files
%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
