# Software Packaging and File Archiving

### Windows

1. Archiving files with Powershell
   ```
   Compress-Archive -Path FILE1, FILE2, FILE3 ZIPFILE.zip
   ```
2. Install and uninstall software using Windows CLI<br>
   * Installing ChocolateyGet
   ```
   Install-Module -Name ChocolateyGet -AllowClobber
   ```
   * Using ChocolateyGet to install
   ```
   Install-Package -Name PACKAGE-NAME -ProviderName ChocolateyGet -Source chocolatey
   ```
   
   Verify installation
   ```
   Get-Package -Name PACKAGE-NAME
   ```

   * Uninstalling
   ```
   Choco Uninstall PACKAGE-NAME
   ```

### Linux

1. Extracting an archive
   ```
   sudo tar -xvf TAR-FILE.tar
   ```
2. Archiving files
   ```
   tar -cvf TAR-FILE.tar FILES
   ```
3. Installing Package
   ```
   sudo apt install PACKAGE-NAME
   ```
   
   Verify installation
   ```
   dpkg -s p7zip-full
   ```
4. Uninstalling Package
   ```
   sudo apt remove PACKAGE-NAME
   ```