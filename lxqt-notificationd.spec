#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-notificationd
Name:		lxqt-notificationd
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	19f4f8a46174f349a3956f0024c5744a
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-notificationd

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-notificationd
%attr(755,root,root) %{_bindir}/lxqt-notificationd
%{_desktopdir}/lxqt-config-notificationd.desktop
#%dir %{_datadir}/lxqt/translations/lxqt-config-notificationd
#%dir %{_datadir}/lxqt/translations/lxqt-notificationd
