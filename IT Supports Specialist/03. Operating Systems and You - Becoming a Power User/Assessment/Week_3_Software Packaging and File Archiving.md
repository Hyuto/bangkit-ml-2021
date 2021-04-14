# Software Packaging and File Archiving

**Graded Assessment : Lab (Qwiklab)**

### Windows

1. Archiving files
   ```
   cd C:\Users\Qwiklab\Documents\
   Compress-Archive -Path Earth, Mercury, Venus Planets.zip
   ```
2. Using ChocolateyGet to install VLC
   ```
   Install-Package -Name vlc -ProviderName ChocolateyGet -Source chocolatey
   Get-Package -Name vlc
   ```
3. Uninstalling GIMP
   ```
   Choco Uninstall GIMP
   Get-Package
   ```

### Linux

1. Installing Atom
   ```
   sudo dpkg -i /home/qwiklab/downloads/atom-amd64.deb
   sudo apt install -f
   dpkg -s atom
   ```
2. Extracting an archive
   ```
   cd /home/qwiklab/downloads
   sudo tar -xvf extract_me.tar
   ```
3. Archiving files
   ```
   cd ~
   tar -cvf Planets.tar --absolute-names /home/qwiklab/documents/Earth /home/qwiklab/documents/Mercury /home/qwiklab/documents/Venus
   ```
4. Installing 7-Zip
   ```
   sudo apt install p7zip-full
   dpkg -s p7zip-full
   ```
5. Uninstalling GIMP
   ```
   sudo apt remove gimp
   dpkg -s gimp
   ```