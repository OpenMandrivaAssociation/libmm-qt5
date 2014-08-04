%define major 5
%define libname %mklibname KF5ModemManagerQt %{major}
%define devname %mklibname -d KF5ModemManagerQt

Summary:	Qt5-only wrapper for ModemManager DBus API
Name:		libmm-qt5
Version:	5.0.91
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libmm-qt
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/5.0.0/libmm-qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(KF5)

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
%{_prefix}/mkspecs/modules/*.pri
%{_libdir}/cmake/KF5ModemManagerQt

#----------------------------------------------------------------------------

%prep
%setup -qn libmm-qt-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

