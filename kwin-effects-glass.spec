# Tag: 6.6.1-2
Name: kwin-effects-glass
Version: 6.6.1
Release: 2%{?dist}
Summary: Glass blur effect for KWin

License: GPL-3.0-or-later
URL: https://github.com/4v3ngR/kwin-effects-glass
Source0: %{url}/archive/6.6.1-2.tar.gz

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
%autosetup -n kwin-effects-glass-6.6.1-2

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
* Fri Feb 27 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.1-2
- adjust projection maxtrix for static blur to handle scaled multi display configurations

* Wed Feb 25 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.1-1
- fix multi-monitor displays when scaling != 100%%

* Wed Feb 25 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.0-3
- add dock comparisons
- update shaders to have improved AA
- remove AA setting
- remove 'window opacity affects blur' setting
- improve shaders for antialias
- Merge pull request #29 from 4v3ngR/fix-antialiased_edges
- hotfix: need to include opacity

* Sat Feb 21 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.0-2
- ensure edge size is <= min half size
- Merge pull request #23 from 4v3ngR/limit_refraction_edge_size
- offset the output by the device origin
- Merge pull request #25 from 4v3ngR/fix_multi_monitor_setups
- hotfix: only apply 'new' device offset translation on 6.6.0
