# Tag: 6.6.2-3
Name: kwin-effects-glass
Version: 6.6.2
Release: 3%{?dist}
Summary: Glass blur effect for KWin

License: GPL-3.0-or-later
URL: https://github.com/4v3ngR/kwin-effects-glass
Source0: %{url}/archive/6.6.2-3.tar.gz

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
%autosetup -n kwin-effects-glass-6.6.2-3

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
* Sat Mar 21 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.2-3
- update README
- rewritten using new blur plugin source code as reference
- reimplement the blacklist/whitelist that was present in the old version
- Update README.md
- Update README.md
- update README and disable X11 builds by default
- deleted
- fixups for floating docks (and maybe menus)
- update frag
- ignore window opacity
- completely ignore window transparency
- need this for fading out menus
- set a minmum minBlurSize to reduce skewing
- some magic numbers, I might make them configuratble one day
- some more shader updates
- some more shader updates
- Update README.md
- some corner cleanups
- Merge branch 'main' of ssh://github.com/4v3ngR/kwin-effects-glass
- updated readme
- remove m_allWindows and include a hack for a bug
- rewrite prePaintWindow to remove the need for several hacks

* Thu Mar 05 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.1-3
- Update README.md
- Merge pull request #34 from vickoc911/main
- add option to exclude docks from tinting
- Merge pull request #35 from 4v3ngR/notint-docks

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
