# Operating Systems and You - Becoming a Power User

## Materi

* Week 1<br>
   1. Introduction to Operating Systems and Becoming a Power User
   2. Basic Commands
   3. File and Text Manipulation
   
   **Note**

   1. Windows CLI & Unix Bash<br>
      * Powershell : [Documentation](https://docs.microsoft.com/powershell/) & [101 guide](https://docs.microsoft.com/powershell/scripting/learn/ps101/00-introduction)
      * [CMD](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
      * [Bash](https://www.gnu.org/software/bash/manual/bash.html)
   2. [Size vs Size of Disk in Windows](https://technet.microsoft.com/en-us/library/hh148159.aspx)
   3. [Bash : Creating, Modifying, and Removing Files and Folders](Assets/Creating,%20Modifying,%20and%20Removing%20Files%20and%20Folders.md)

   **Assessment** : [Creating, Modifying, and Removing Files and Folders](Assessment/Week_1_01%20Creating,%20Modifying,%20and%20Removing%20Files%20and%20Folders.md)
* Week 2<br>
   1. Users and Groups
   2. Permissions
   
   **Note**

   1. [Windows ACL](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374872(v=vs.85).aspx)
   2. [Special Permissions in Windows](https://technet.microsoft.com/en-us/library/cc732880(v=ws.11).aspx)
   3. [Note : Permissions](Assets/Creating,%20Modifying,%20and%20Removing%20File%20and%20Folder%20Permissions.md)

   **Assessment** : [Creating, Modifying, and Removing File and Folder Permissions](Assessment/Week_2_Creating,%20Modifying,%20and%20Removing%20File%20and%20Folder%20Permissions.md)
* Week 3<br>
   1. Software Distribution
   2. Package Managers
   3. What’s happening in the background?
   4. Device Software Management
   
   **Note**

   1. Windows Software Packages
      * [Portable Executable](https://en.wikipedia.org/wiki/Portable_Executable)
      * [Installation Package](https://msdn.microsoft.com/en-us/library/windows/desktop/aa369294(v=vs.85).aspx)
      * [Windows Store](https://en.wikipedia.org/wiki/Windows_Store)
      * [App Packager (MakeAppx.exe)](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446767(v=vs.85).aspx)
   2. [7-Zip](http://www.7-zip.org/download.html) and [PowerShell Zips](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-5.0)
   3. [Linux Tar Command](http://www.linfo.org/tar.html)
   4. Windows Package Dependencies
      * [Dynamic- link library](https://en.wikipedia.org/wiki/Dynamic-link_library)
      * [DLL Hell](https://en.wikipedia.org/wiki/DLL_Hell)
      * [Side- by- side Assemblies](https://msdn.microsoft.com/en-us/library/aa376307.aspx)
   5. Linux Package Dependencies : *[dpkg](https://help.ubuntu.com/lts/serverguide/dpkg.html)*
   6. Windows Package Managers
      * [NuGet](https://en.wikipedia.org/wiki/NuGet)
      * [Chocolatey](https://chocolatey.org/packages)
   7. [Linux PPAs](https://help.launchpad.net/Packaging/PPA)
   8. [GIMP](https://www.gimp.org/downloads/)
   9. [Note : Software Packaging and File Archiving](Assets/Software%20Packaging%20and%20File%20Archiving.md)

   **Assessment** : [Software Packaging and File Archiving](Assessment/Week_3_Software%20Packaging%20and%20File%20Archiving.md)
* Week 4<br>
   1. Filesystem types

   **Note**

   1. [FAT32 File System](https://support.microsoft.com/en-us/help/154997/description-of-the-fat32-file-system)
   2. Disk Partitioning and Formatting in Windows
      * [Allocation unit size when formatting a disk](https://support.microsoft.com/en-us/help/140365/default-cluster-size-for-ntfs--fat--and-exfat)
      * *[DiskPart](https://technet.microsoft.com/en-us/library/cc766465(v=ws.10).aspx)*
   3. [Mounting and Unmounting a Filesystem in Linux](https://en.wikipedia.org/wiki/Fstab)
   4. [Windows Paging](https://en.wikipedia.org/wiki/Paging#Windows_NT)
   5. [Linux Swap](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Installation_Guide/s2-diskpartrecommend-ppc.html#id4394007)
   6. NTFS File System : [Master File Table](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365230(v=vs.85).aspx), [Creating Symbolic Links](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363878(v=vs.85).aspx), and [Hard Links and Junctions](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365006(v=vs.85).aspx).
   7. [Linux Disk Usage](https://www.howtogeek.com/115229/htg-explains-why-linux-doesnt-need-defragmenting/)
   8. [Linux Filesystem Repair](https://en.wikipedia.org/wiki/Fsck)
   9. Linux : [Partitioning and Formatting a Disk Drive](Assets/Partitioning%20and%20Formatting%20a%20Disk%20Drive.md)

   **Assessment** : [Partitioning and Formatting a Disk Drive](Assessment/Week_4_Partitioning%20and%20Formatting%20a%20Disk%20Drive.md)
* Week 5<br>
  1. Life of a Process
  2. Managing Processes
  3. Process Utilization
   
   **Note**

   1. Process Creation and Termination in Windows : *[taskkill](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill)*
   2. Process Information<br>
      * Windows : *[get-process](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-5.1)*
      * Linux : *[ps](http://man7.org/linux/man-pages/man1/ps.1.html)*
   3. [Windows Signal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/signal)
   4. [Managing Processes in Windows](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)
   5. Resource Monitoring
      * [Windows](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-5.1#outputs)
      * [Linux](https://en.wikipedia.org/wiki/Load_(computing))
   6. [Note : Maintain Efficient Process Utilization](Assets/Maintain%20Efficient%20Process%20Utilization.md)
   
   **Assessment** : [Maintain Efficient Process Utilization](Assessment/Week_5_Maintain%20Efficient%20Process%20Utilization.md)
* Week 6<br>
  1. Remote Access
  2. Virtualization
  3. Logging
  4. Operating System Deployment

   **Note**
   1. Remote Connections in Windows
      * [Powershell](https://blogs.msdn.microsoft.com/powershell/2015/06/03/looking-forward-microsoft-support-for-secure-shell-ssh/)
      * [Comparison of SSH clients](https://en.wikipedia.org/wiki/Comparison_of_SSH_clients)
      * [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
   2. [Remote Connection File Transfer in Windows](https://technet.microsoft.com/en-us/library/hh750728(v=ws.11).aspx)
   3. Virtual Machines
      * [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
      * [VirtualBox Manual](https://www.virtualbox.org/manual/ch01.html)
      * [Comparison of platform virtualization software](https://en.wikipedia.org/wiki/Comparison_of_platform_virtualization_software)
   4. [Linux Logs](http://manpages.ubuntu.com/manpages/zesty/man8/logrotate.8.html)
   5. [OS Deployment Methods](https://en.wikipedia.org/wiki/Comparison_of_disk_cloning_software)
   6. [Note : Using Logs to Help You Track Down an Issue](Assets/Using%20Logs%20to%20Help%20You%20Track%20Down%20an%20Issue.md)
   
   **Assessment** : [Using Logs to Help You Track Down an Issue](Assessment/Week_6_Using%20Logs%20to%20Help%20You%20Track%20Down%20an%20Issue.md)