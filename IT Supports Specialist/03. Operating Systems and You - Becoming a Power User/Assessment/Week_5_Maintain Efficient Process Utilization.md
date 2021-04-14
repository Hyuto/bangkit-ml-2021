# Maintain Efficient Process Utilization

**Graded Assessment : Lab (Qwiklab)**

### Windows

1. Terminating a specific process
   ```
   Get-Process -Name "totally_not_malicious"
   taskkill /F /PID [PROCESS ID]
   Get-Process -Name "totally_not_malicious"
   ```
2. Terminating multiple processes
   ```
   Get-Process -Name "*razzle*"
   taskkill /F /PID [PROCESS ID]
   Get-Process -Name "*razzle*"
   ```

### Linux

1. Terminating a specific process
   ```
   ps -aux | grep "totally_not_malicious"
   sudo kill [PROCESS ID]
   ps -aux | grep "totally_not_malicious"
   ```
2. Terminating multiple processes
   ```
   ps -aux | grep "razzle"
   sudo kill [PROCESS ID]
   ps -aux | grep "razzle"
   ```