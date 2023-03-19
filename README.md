# SailfishOS:Chum GUI Installer

**The SailfishOS:Chum GUI Installer performs the initial installation of the [SailfishOS:Chum GUI application](https://github.com/sailfishos-chum/sailfishos-chum-gui#readme). SailfishOS:Chum GUI Installer selects, downloads and installs the correct variant of the SailfishOS:Chum GUI application built for the CPU-architecture of the device and the installed SailfishOS release from the SailfishOS-OBS.**

The SailfishOS:Chum GUI Installer works on any SailfishOS release ≥&nbsp;3.1.0 and all supported CPU-architectures (armv7hl, i486 and aarch64).  The current SailfishOS:Chum GUI Installer RPM can be obtained from [its "latest release" page at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui-installer/releases/latest), [OpenRepos.net](https://openrepos.net/content/olf/sailfishos-chum-gui-installer) and [the SailfishOS-OBS](https://build.merproject.org/package/show/sailfishos:chum/sailfishos-chum-gui-installer).

### Important notes

* If you experience issues with the SailfishOS:Chum GUI Installer, please take a look at its log file `/var/log/sailfishos-chum-gui-installer.log.txt`.  If that does not reveal to you what is going wrong, please check first if an issue report describing this issue [is already filed at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui-installer/issues), then you might file a new issue report there and attach the log file to it, or enhance an extant bug report.
* If you experience issues when installing, removing or updating packages after a SailfishOS upgrade, try running `devel-su pkcon refresh` in a terminal app.
* When the SailfishOS:Chum GUI Installer fails to install anything (i.e, a minute after installing it the icon of the SailfishOS:Chum GUI application has not appeared on the launcher / desktop), most likely the preceding or the following bullet point is the reason.
* Before software can be build for a SailfishOS release at the SailfishOS-OBS, Jolla must create a [corresponding "download on demand (DoD)" OBS-repository](https://build.merproject.org/project/subprojects/sailfishos).  It may take a little time after a new SailfishOS release is published before the corresponding "DoD" repository is being made available, during which installing the SailfishOS:Chum GUI application by the SailfishOS:Chum GUI Installer or updating the SailfishOS:Chum GUI application by itself on a device with the new SailfishOS release already installed will not work, because the SailfishOS:Chum GUI application cannot be compiled for this new SailfishOS release by the Sailfish-OBS, yet; consequently this is always the case for "closed beta (cBeta)" releases of SailfishOS.  In such a situation one has to manually download the SailfishOS:Chum GUI application built for the last prior SailfishOS "general availability (GA)" release (e.g., from [its releases section at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui/releases) or [the SailfishOS:Chum repository](https://build.merproject.org/project/show/sailfishos:chum/sailfishos-chum-gui)), then install or update the SailfishOS:Chum GUI application via `pkcon install-local <downloaded RPM file>`, and hope that there is no change in the new SailfishOS release which breaks the SailfishOS:Chum GUI application; if there is, please report that soon at [the SailfishOS:Chum GUI application's issue tracker](https://github.com/sailfishos-chum/sailfishos-chum-gui/issues).
* Disclaimer: The SailfishOS:Chum GUI application and its installer may still have flaws, kill your kittens or break your SailfishOS installation!  Although this is very unlikely after years of testing by many users, new flaws may be introduced in any release (as for any software).  Mind that the license you implicitly accept by using the SailfishOS:Chum GUI application or the SailfishOS:Chum GUI Installer excludes any liability.


### Installation instructions

* **Installation via Storeman**
  1. Search for *Installer*.
  2. Select the *SailfishOS:Chum GUI Installer* by *olf*.
  3. Enable olf's repository in the top pulley menu.
  4. Install *SailfishOS:Chum GUI Installer*.

* **Initial installation without having Storeman installed**
  1. Enable "System → Security → Untrusted software → Allow untrusted software" in the SailfishOS Settings app.
  2. Download the current SailfishOS:Chum GUI Installer RPM from [its "latest release" page at GitHub](https://github.com/storeman-developers/harbour-storeman-installer/releases/latest), [OpenRepos.net](https://openrepos.net/content/olf/sailfishos-chum-gui-installer) or [the SailfishOS:Chum repository](https://build.merproject.org/project/show/sailfishos:chum/sailfishos-chum-gui-installer).
  3. Tap on the "File downloaded" notification on your SailfishOS device or select the downloaded RPM file in a file-manager app and choose "Install" in its pulley menu; then confirm the installation.
  4. Preferably disable "Allow untrusted software" again.

### Features of SailfishOS:Chum GUI Installer

* SailfishOS:Chum GUI Installer creates a persistent log file `/var/log/sailfishos-chum-gui-installer.log.txt`.
* SailfishOS:Chum GUI Installer runs "unattended": I.e., without any manual steps, after its installation has been triggered, until the SailfishOS:Chum GUI application is installed.
* SailfishOS:Chum GUI Installer is slow, because it calls `pkcon` three times, which acts quite slowly.  The minimal run time for SailfishOS:Chum GUI Installer  is about 7 seconds, the typical run time is rather 10 seconds (measured from the moment SailfishOS:Chum GUI Installer's installation has been triggered, until ultimately the SailfishOS:Chum GUI application is installed).  This is already a lot, but I rarely experienced a stalled Packagekit daemon (for which `pkcon` is just a command line frontend, communicating with the daemon via D-Bus) during heavy testing, which can be observed with the crude `pkmon` utility (`Ctrl-C` gets you out.:smiley:), so SailfishOS:Chum GUI Installer tries to detect these "hangs" and to counter them: If that happens, its run time can be up to slightly more than 1 minute.  In the worst case a stalled PackageKit daemon (and with it its `pkcon` client process(es)) stalls SailfishOS:Chum GUI Installer, until the PackageKit daemon reaches its idle time out of 300 seconds (5 minutes; this could theoretically happen three times, resulting in a likely unsuccessful run time of more than 15 minutes).
