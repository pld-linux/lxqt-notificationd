#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-notificationd
Name:		lxqt-notificationd
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	ac178f02150fac3585096bd28a28d13e
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 1.0.0
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
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-notificationd
%attr(755,root,root) %{_bindir}/lxqt-notificationd
%{_desktopdir}/lxqt-config-notificationd.desktop
