# Installing, Updating, and Removing Software

**Graded Assessment : Lab (Qwiklab)**

### 1. Windows

Using GUI

### 2. Linux

* Verifying installed software on Linux
    ```
    dpkg -s firefox-esr
    dpkg -s gimp
    dpkg -s vlc
    ```
* Updating VLC Media Player
    ```
    sudo apt-get install -f
    dpkg -s vlc
    ```
* Installing Mozilla Firefox
    ```
    sudo apt-get update
    sudo apt-get install firefox-esr
    dpkg -s firefox-esr
    ```
* Uninstalling GIMP
    ```
    sudo apt-get remove gimp
    dpkg -s gimp
    ```