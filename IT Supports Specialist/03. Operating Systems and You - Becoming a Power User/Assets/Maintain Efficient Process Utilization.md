# Maintain Efficient Process Utilization

### Windows

1. Get process id by name
   ```
   Get-Process -Name NAME
   ```
2. Terminating a specific process
   ```
   taskkill /F /PID [PROCESS ID]
   ```

### Linux

1. Get process id by name
   ```
   ps -aux | grep NAME
   ```
2. Terminating a specific process
   ```
   sudo kill [PROCESS ID]
   ```