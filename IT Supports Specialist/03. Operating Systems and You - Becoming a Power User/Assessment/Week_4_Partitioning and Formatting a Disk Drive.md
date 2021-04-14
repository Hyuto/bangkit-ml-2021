# Partitioning and Formatting a Disk Drive

**Graded Assessment : Lab (Qwiklab)**

### Windows

Using GUI

### Linux

1. Creating Partitions
   ```
   sudo fdisk /dev/sdb

   key :
   d : 12x
   n
   enter : 2x
   2097200
   n
   enter : 3x
   t
   1
   19
   w
   ```
2. Formatting partitions using mkfs
   ```
   sudo mkfs -t ext4 /dev/sdb2
   sudo mount /dev/sdb2 /home/my_drive
   ```