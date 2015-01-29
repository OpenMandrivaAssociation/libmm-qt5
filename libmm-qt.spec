%define major 5
%define libname %mklibname KF5ModemManagerQt %{major}
%define devname %mklibname -d KF5ModemManagerQt
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Qt5-only wrapper for ModemManager DBus API
Name:		libmm-qt5
Version:	5.2.0
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libmm-qt
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{plasmaver}/libmm-qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(ECM)
BuildRequires:	ninja

%description
Qt library for ModemManager.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt-only wrapper for ModemManager DBus API
Group:		System/Libraries
Conflicts:	%{_lib}mm-qt0 < 1:0.5.0
Obsoletes:	%{_lib}mm-qt0 < 1:0.5.0

%description -n %{libname}
Qt library for ModemManager.

%files -n %{libname}
%{_libdir}/libKF5ModemManagerQt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(ModemManager)
Conflicts:	%{_lib}mm-qt-devel < 1:0.5.0
Obsoletes:	%{_lib}mm-qt-devel < 1:0.5.0

%description -n %{devname}
Qt libraries and headers for developing applications that use ModemManager.

%files -n %{devname}
%doc README
%{_includedir}/KF5/ModemManagerQt
%{_includedir}/KF5/modemmanagerqt_version.h
%{_libdir}/libKF5ModemManagerQt.so
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5ModemManagerQt

#----------------------------------------------------------------------------

%prep
%setup -qn libmm-qt-%{plasmaver}

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

