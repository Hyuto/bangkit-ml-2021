# Using Logs to Help You Track Down an Issue

**Graded Assessment : Lab (Qwiklab)**

### Windows

Viewing logs on Windows : Using GUI

### Linux

1. Viewing logs on Linux
   ```
   ls /var/log
   sudo cat /var/log/syslog | grep "Qwiklab Error"
   ```
2. Fix low disk space
   ```
   sudo du -a /home | sort -n -r | head -n 5
   sudo rm /home/lab/storage/ultra_mega_large.txt
   ```
3. Remove corrupted file
   ```
   sudo rm /home/lab/corrupted_file
   ```
4. Update VLC
   ```
   sudo apt update && sudo apt install vlc
   ```
5. End malicious processes
   ```
   ps -aux | grep "totally_not_malicious"
   sudo kill [PROCESS ID]
   ```
6. Change permission of secret file to public (777)
   ```
   sudo chmod 777 super_secret_file.txt
   ```