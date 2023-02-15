Summary:        Installs SailfishOS:Chum GUI application
License:        LGPL-2.1-only
Name:           sailfishos-chum-gui-installer
# The Git release tag format must adhere to just <version>.  The <version>
# field adheres to semantic versioning and the <release> field comprises a
# natural number greater or equal to 1, which may be prefixed with one of
# {alpha,beta,rc,release} (e.g., "beta3").  For details and reasons, see
# https://github.com/storeman-developers/harbour-storeman-installer/wiki/Git-tag-format
Version:        0.3.1
Release:        1
Group:          Applications/System
URL:            https://github.com/sailfishos-chum/%{name}
# The "Source0:" line below requires that the value of %%{name} is also the
# project name at GitHub and the value of %%{version} is also the name of a
# correspondingly set git-tag.
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Note that the rpmlintrc file must be named so according to
# https://en.opensuse.org/openSUSE:Packaging_checks#Building_Packages_in_spite_of_errors
Source99:       %{name}.rpmlintrc 
BuildArch:      noarch
# For details on "Requires:" statements, especially "Requires(a,b,c):", see:
# https://rpm-software-management.github.io/rpm/manual/spec.html#requires
# Most of the following dependencies are required for both, specifically for
# the %%post scriptlet and additionally as a general requirement after the RPM
# transaction has finished, but shall be already installed on SailfishOS:
Requires:       ssu
Requires(post): ssu
Requires:       PackageKit
Requires(posttrans): PackageKit
# `or` was introduced with RPM 4.13, SailfishOS v2.2.1 started deploying v4.14:
# https://together.jolla.com/question/187243/changelog-221-nurmonjoki/#187243-rpm
# But the SailfishOS-OBS' does not support `or`, either due to the antique OBS
# release or `tar_git`: https://github.com/MeeGoIntegration/obs-service-tar-git
# ToDo: Check if the GNU-versions of these packages (named as alternatives below)
# also provide the aliases ("virtual packages") denoted here, then these can be
# used; ultimately most of these packages shall be already installed, anyway.
# 1. `coreutils` (for e.g., `touch` and many other very basic UNIX tools):
# Requires:       (busybox-symlinks-coreutils or gnu-coreutils)
Requires:       coreutils
# Requires(post,posttrans): (busybox-symlinks-coreutils or gnu-coreutils)
Requires(post): coreutils
Requires(posttrans): coreutils
# 2. `util-linux` for `setsid`:
Requires:       util-linux
Requires(posttrans): util-linux
# 3. `psmisc` for `killall`:
# Requires:       (busybox-symlinks-psmisc or psmisc-tools)
Requires:       psmisc
# Requires(posttrans): (busybox-symlinks-psmisc or psmisc-tools)
Requires(posttrans): psmisc
# 4. `procps` for `pkill` / `pgrep`: Used `killall` instead, which suits better here.
# Requires:       (busybox-symlinks-procps or procps-ng)
#Requires:       procps
# Requires(posttrans): (busybox-symlinks-procps or procps-ng)
#Requires(posttrans): procps
# The oldest SailfishOS release which SailfishOS:Chum supports, because it is the
# oldest useable DoD-repo at https://build.merproject.org/project/subprojects/sailfishos
Requires:       sailfish-version >= 3.1.0
# Provide (anti-)dependencies to sibling packages:
Conflicts:      sailfishos-chum
Obsoletes:      sailfishos-chum
Conflicts:      sailfishos-chum-testing
Obsoletes:      sailfishos-chum-testing
Provides:       sailfishos-chum-repository

# %%global screenshots_url    https://github.com/sailfishos-chum/sailfishos-chum-gui/raw/main/.xdata/screenshots/
%global logdir             %{_localstatedir}/log
%global logfile            %{logdir}/%{name}.log.txt

# This %%description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%description
SailfishOS:Chum GUI Installer selects, downloads and installs the right variant
of the SailfishOS:Chum GUI application built for the CPU-architecture
of the device and its installed SailfishOS release.

%if 0%{?_chum}
PackageName: SailfishOS:Chum GUI Installer
Type: desktop-application
Categories:
 - System
 - Utility
 - Network
 - Settings
 - PackageManager
DeveloperName: olf (Olf0)
Custom:
  Repo: %{url}
Icon: %{url}/raw/main/.icons/%{name}.svg  #Screenshots: - %%{screenshots_url}sailfishos-chum-gui-01.png
Url:
  Homepage: https://openrepos.net/content/olf/sailfishoschum-gui-installer
  Help: %{url}/issues
  Bugtracker: %{url}/issues
%endif

%define _binary_payload w6.gzdio
%define _source_payload w2.gzdio

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp bin/%{name} %{buildroot}%{_bindir}/

%post
# The %%post scriptlet is deliberately run when installing and updating.
# Create a persistent log file, i.e., which is not managed by RPM and hence
# is unaffected by removing the %%{name} RPM package:
if [ ! -e %{logfile} ]
then
  curmask="$(umask)"
  umask 022
  [ ! -e %{logdir} ] && mkdir -p %{logdir}
  umask 113
  touch %{logfile}
  # Not necessary, because umask is set:
  # chmod 0664 %%{logfile}
  chgrp ssu %{logfile}
  umask "$curmask"
fi
# The added sailfishos-chum repository is not removed when SailfishOS:Chum GUI
# Installer is removed, but when the SailfishOS:Chum GUI application is removed.
ssu ar sailfishos-chum 'https://repo.sailfishos.org/obs/sailfishos:/chum/%%(release)_%%(arch)/'
ssu ur
# BTW, `ssu`, `rm -f`, `mkdir -p` etc. *always* return with "0" ("success"), hence
# no appended `|| true` needed to satisfy `set -e` for failing commands outside of
# flow control directives (if, while, until etc.).  Furthermore on Fedora Docs it
# is indicated that solely the final exit status of a whole scriptlet is crucial: 
# See https://docs.pagure.org/packaging-guidelines/Packaging%3AScriptlets.html
# or https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/#_syntax
# committed on 18 February 2019 by tibbs ( https://pagure.io/user/tibbs ) in
# https://pagure.io/packaging-committee/c/8d0cec97aedc9b34658d004e3a28123f36404324
# Hence I have the impression, that only the main section of a spec file is
# interpreted in a shell called with the option `-e', but not the scriptlets
# (`%%pre*`, `%%post*`, `%%trigger*` and `%%file*`).
exit 0

%postun
if [ "$1" = 0 ]  # Removal
then
  ssu rr sailfishos-chum
  rm -f /var/cache/ssu/features.ini
  ssu ur
fi
exit 0

%posttrans
# At the very end of every install or upgrade
# The sailfishos-chum-gui-installer script must be started fully detached
# (by a double-fork / "daemonize") to allow for this RPM transaction
# to finalise (what waiting for it to finish would prevent).
# (Ab)using the %%posttrans' interpreter instance for the preamble:
umask 113
# [ "$PWD" = / ] || cd /  # Set PWD to /, if not already; omitted,
# because the scriptlets are executed with PWD safely set to /.
setsid --fork sh -c '(%{_bindir}/%{name} "$1" "$2")' sh_call_inst-chum-gui "$$" "%{logfile}" >> "%{logfile}" 2>&1 <&-
# The first 15 characters of the spawned process' name
# (to be used for, e.g., `ps` and `pgrep` / `pkill`) are:
# sh_call_inst-ch
exit 0

%files
%attr(0754,root,ssu) %{_bindir}/%{name}

%changelog
* Thu Sep  9 1999 olf <Olf0@users.noreply.github.com> - 99.99.99
- See %{url}/releases
