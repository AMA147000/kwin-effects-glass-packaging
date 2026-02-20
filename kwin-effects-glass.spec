# Tag: 6.6.0-1-test
Name: kwin-effects-glass
Version: 6.6.0
Release: 1%{?dist}
Summary: Glass blur effect for KWin

License: GPL-3.0-or-later
URL: https://github.com/4v3ngR/kwin-effects-glass
Source0: %{url}/archive/6.6.0-1.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: kwin-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: libepoxy-devel
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kdecoration-devel
BuildRequires: wayland-devel
BuildRequires: libdrm-devel

Requires: kwin

%description
Fork of the Plasma 6 blur effect with additional features (including force blur) and bug fixes.

%prep
%autosetup -n kwin-effects-glass-%{version}

%build
%cmake
%cmake_build

%check
# No tests available

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/qt6/plugins/kwin/effects/configs/*.so
%{_libdir}/qt6/plugins/kwin/effects/plugins/*.so

%changelog
%autochangelog
