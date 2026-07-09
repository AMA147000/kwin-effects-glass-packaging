# Tag: 20260620-1
Name: kwin-effects-glass
Version: 20260620
Release: 1.2%{?dist}
Summary: Glass blur effect for KWin

License: GPL-3.0-or-later
URL: https://github.com/4v3ngR/kwin-effects-glass
Source0: %{url}/archive/20260620-1.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: qt6-qtbase-devel
BuildRequires: kwin-devel
BuildRequires: libplasma-devel
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
%autosetup -n kwin-effects-glass-20260620-1

%build
%cmake
%cmake_build

%check
# No tests available

%install
%cmake_install

%find_lang kwin_effects_glass

%files -f kwin_effects_glass.lang
%license LICENSE
%doc README.md
%{_libdir}/qt6/plugins/kwin/effects/configs/*.so
%{_libdir}/qt6/plugins/kwin/effects/plugins/*.so

%changelog
* Sat Jun 20 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 20260620-1
- don't ignore all spectacle windows
- Merge branch 'main' of github.com:4v3ngR/kwin-effects-glass
- fix effect for floating docks
- load core shaders - this may break for legacy systems

* Fri Jun 19 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 20260619-1
- more customisation settings
- more settings
- add config to exclude tinting from decorations
- allow tooltip tint exclusion
- rounded content corners
- add option to ignore application provided blur regions
- updated README
- calculate rounded content region radius based on window decoration width
- remove broken optimization for when blur/noise settings are the same
- feat(blur): add finetune slider that scales sample offsets
- feat(blur): match downsample/upsample kernels for smoother dual-Kawase blur
- tweak: bump BlurFinetune
- feat(blur): saturation compensation - keep vibrant colors at highter blur radii
- tweak: saturation boost and weighting
- Merge pull request #78 from PKMNPlatin/feature/blur-finetune
- chore: made blur color compensation toggelable since it can cause artifacts
- fix(snells-glass): smooth corners for non-rounded windows
- chore: extract glass refraction + outline into functions, add GlassFragment so the outline can vary per algorithm
- feat(glass): Snell's lens slope follows refractionNormalPow to match the shape settings better
- feat(blur): apply saturation in OKLab option
- Merge pull request #80 from PKMNPlatin/feature/blur-finetune
- Merge pull request #81 from PKMNPlatin/feature/physically-based-refraction
- fix(oklab): clamp srgb input
- Merge pull request #82 from PKMNPlatin/feature/oklab-color-space
- feat(refraction): add bevel intensity slider for snells path
- fix(refraction): fixed normals
- Merge pull request #85 from PKMNPlatin/feature/physically-based-refraction
- only round the contents blur corner if the window has a visible decoration
- change highlight to match the new liquid glass widgets
- fix: support KWin 6.7 effect API
- fix: tighten KWin 6.7 blur fallback
- fix: keep Wayland blur geometry global
- Merge pull request #87 from avitretiak/fix/kwin-6-7-compat
- Update README.md

* Wed Jun 03 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 20260602-01
- feature: prepare toggleable physically based (snells law) refraction shader branch
- feature: implemented physically based refraction + new uniform slider especially for the physical-based toggle
- Merge pull request #75 from PKMNPlatin/feature/physically-based-refraction
- fix maximized rounded corners setting
- fixups for dynamic corners

* Sun May 31 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 20260531-01
- explicitly set window border radius
- add option to apply blur to contents only
- don't consider contentShape
- fix up frame blur exclusion when there's no content region
- Update blur settings. Now content and decoration can have different blur and noise levels

* Thu May 28 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 20260527-01
- improve corner refraction
- Merge branch 'main' of github.com:4v3ngR/kwin-effects-glass
- Added localization support as well as french translation.
- Removed a bunch of unused dependencies
- Added translation references and author
- Merge pull request #69 from RubisetCie/french-translation
- hardcode spactacle to the exclusion list
- add xwaylandvideobridge to blacklist

* Sun May 24 2026 AMA147000 - 6.6.4-1.1
- Manual update to build for plasma 6.6.5

* Mon Apr 27 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.4-1
- Option to disable edge brighter in panels and tooltips
- Option to disable edge brighter in panels and tooltips
- Merge pull request #62 from vickoc911/disable_brighter_dock
- window corner radius will change when corner is touching the edge of another window
- only consider current activity
- fix blur artifacts on 6.4.4
- need the prePaintWindow functions even for 6.4.4
- Update README.md

* Tue Apr 14 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.3-2
- chore: add /build to .gitignore
- Merge branch '4v3ngR:main' into main
- Refactor blur effect and shader files for improved performance and organization
- fix: bring back corner radius handling for on-screen displays and tooltips
- Merge pull request #57 from PKMNPlatin/cleanup/shader-generation
- edge effect
- edge lighting and shadow - pt1
- slight tweaks
- thinner
- wrap in glowStrength check
- fix if statement
- change the light reflection
- we should only apply the blur if we're within the rounded rect
- don't apply glow to docks if the radius is too big for the dock
- don't have edge lighting on small docks
- fix: keep compatibility with X11 (Xlibre) and KDE 6.6
- Merge pull request #60 from xlab/fix/x11-xlibre-build-6.6

* Wed Apr 01 2026 github-actions[bot] <github-actions[bot]@users.noreply.github.com> - 6.6.3-1
- simplify shaders
- fix window corners
- remove shortcuts that produced uncleen edges

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
