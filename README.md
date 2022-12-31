# SailfishOS:Chum GUI Installer

**The SailfishOS:Chum GUI Installer performs the initial installation of the [SailfishOS:Chum GUI application](https://github.com/sailfishos-chum/sailfishos-chum-gui). SailfishOS:Chum GUI Installer selects, downloads and installs the correct variant of the SailfishOS:Chum GUI application built for the CPU-architecture of the device and the installed SailfishOS release from the SailfishOS-OBS.**

The SailfishOS:Chum GUI Installer works on any SailfishOS release ≥&nbsp;3.1.0 and all supported CPU-architectures (armv7hl, i486 and aarch64).  The current SailfishOS:Chum GUI Installer RPM can be obtained from [its "latest release" page at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui-installer/releases/latest), [OpenRepos.net](https://openrepos.net/content/olf/sailfishos-chum-gui-installer) and [the SailfishOS-OBS](https://build.merproject.org/package/show/sailfishos:chum/sailfishos-chum-gui-installer).

### Important notes

* If you experience issues with SailfishOS:Chum GUI Installer, please take a look at its log file `/var/log/sailfishos-chum-gui-installer.log.txt`.  If that does not reveal to you what is going wrong, please check first if an issue report describing this issue [is already filed at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui-installer/issues), then you might file a new issue report there and attach the log file to it, or enhance an extant bug report; alternatively (but this is really a much worse choice) and usually with much longer response times and no real issue tracking due to the lack of any integration, you can describe your issue in [a comment at OpenRepos](https://openrepos.net/content/olf/sailfishos-chum-gui-installer#comments) with a link to your log file copied to a data-sharing service like Pastebin etc.
* If you experience issues when installing, removing or updating packages after a SailfishOS upgrade, try running `devel-su pkcon refresh` in a terminal app.
* Before software can be build for a SailfishOS release at the SailfishOS-OBS, Jolla must create a corresponding "download on demand (DoD)" OBS-repository.  It might take some time after a new "general availability (GA)" SailfishOS release is published before the corresponding "DoD" repository is being made available, during which installing or updating the SailfishOS:Chum GUI application by itself or the SailfishOS:Chum GUI Installer on a device with the new SailfishOS release already installed will not succeed, because the SailfishOS:Chum GUI application cannot be compiled for this new SailfishOS release by the Sailfish-OBS, yet; consequently this is always the case during the "closed beta (cBeta)" and "early access (EA)" phases of a new SailfishOS release.  

<ToDo>
Hence one has to manually download and install, or update the SailfishOS:Chum GUI application built for the last prior SailfishOS GA via `pkcon install-local <downloaded RPM file>` release (e.g., from [its releases section at GitHub](https://github.com/sailfishos-chum/sailfishos-chum-gui-installer/releases) or [the SailfishOS:Chum repository](https://build.merproject.org/project/show/sailfishos:chum/sailfishos-chum-gui-installer)) then, and hope that there is no change in the new SailfishOS release, which breaks the SailfishOS:Chum GUI application; if there is, please report that soon at [the SailfishOS:Chum GUI application's issue tracker](https://github.com/sailfishos-chum/sailfishos-chum-gui/issues).
</ToDo>
* Disclaimer: The SailfishOS:Chum GUI application and SailfishOS:Chum GUI Installer may still have flaws, kill your kittens or break your SailfishOS installation!  Although this is very unlikely after years of testing by many users, new flaws may be introduced in any release (as for any software).  Be aware, that the license you implicitly accept by using the SailfishOS:Chum GUI and its installer excludes any liability.


<ToDo:>
### Installation instructions

* Initial installation without having Storeman or SailfishOS:Chum already installed
  1. Enable "System → Security → Untrusted software → Allow untrusted software" in the SailfishOS Settings app.
  2. Download the current Storeman Installer RPM from [its "latest release" page at GitHub](https://github.com/storeman-developers/harbour-storeman-installer/releases/latest), [OpenRepos.net](https://openrepos.net/content/olf/storeman-installer) or [the SailfishOS-OBS](https://build.merproject.org/package/show/home:olf:harbour-storeman/harbour-storeman-installer).
  3. Tap on the "File downloaded" notification on your SailfishOS device or select the downloaded RPM file in a file-manager app and choose "Install" in its pulley menu; then confirm the installation.
  4. Preferably disable "Allow untrusted software" again.

* Installation via Storeman (i.e., updating from Storeman <&nbsp; 0.2.9)
  * <sup>If you have [olf's repository at OpenRepos](https://openrepos.net/user/5928/programs) enabled, *Storeman Installer* shall be offered as an update candidate for the outdated *Storeman* installed: Just accept this offer.<br />Otherwise:</sup>
  1. Search for *Installer*.
  2. Select the *Storeman Installer* by *olf*.
  3. Enable olf's repository in the top pulley menu.
  4. Install *Storeman Installer*.

* Installation via SailfishOS:Chum GUI application
  1. Search for *Installer* in "Applications".
  2. Select *Storeman Installer*.
  3. Install *Storeman Installer*.

### Features of Storeman Installer

* The Storeman Installer is automatically removed ("uninstalled") when Storeman is being installed.
* [Storeman Installer 1.3.1](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.1) and all later versions are offered as an update candidate for Storeman, if an RPM repository is enabled, which offers the *harbour-storeman-installer* package and Storeman (*harbour-storeman* package) <&nbsp;0.2.99 is already installed.
* Installing [Storeman Installer 1.3.1](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.1) and all later versions also automatically removes an installed Storeman (*harbour-storeman* package) <&nbsp;0.2.99, which eliminates the former necessity to manually remove ("uninstall") an old Storeman. 
* [Storeman Installer 1.3.8](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.8) and all later versions create a persistent log file `/var/log/harbour-storeman-installer.log.txt`.
* Storeman Installer 2 runs "unattended": I.e., without any manual steps, after its installation has been triggered, until Storeman is installed.
* Storeman Installer is slow, because it calls `pkcon` two (releases before v1.3.8) to three times (releases from v[1.3.8](https://github.com/storeman-developers/harbour-storeman-installer/releases/tag/1.3.8) on), which acts quite slowly.  The minimal run time for Storeman Installer 2 is about 7 seconds, the typical run time is rather 10 seconds (measured from the moment Storeman Installer's installation has been triggered, until ultimately Storeman is installed).  This is already a lot, but I rarely experienced a stalled Packagekit daemon (for which `pkcon` is just a command line frontend, communicating with the daemon via D-Bus) during heavy testing, which can be observed with the crude `pkmon` utility (`Ctrl-C` gets you out.:smiley:), so Storeman Installer now tries to detect these "hangs" and to counter them: If that happens, its run time can be up to slightly more than 1 minute.  In the worst case a stalled PackageKit daemon (and with it its `pkcon` client process(es)) stalls Storeman Installer, until the PackageKit daemon reaches its idle time out of 300 seconds (5 minutes; this could theoretically happen three times, resulting in a likely unsuccessful run time of more than 15 minutes).
