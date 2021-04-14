# Partitioning and Formatting a Disk Drive

### Blocks and partitions

1. Blocks<br>
   Blocks are a layer of storage devices that allow individual access to each independently. They allow programs to access storage without worrying about whether the underlying hardware device is a hard drive, solid state drive, flash drive, etc. View block devices and file systems attached to system using the `lsblk` command. This command gathers information about all devices attached to the system, and prints them out using a tree-like structure. To view the devices attached to your VM, use the `lsblk` command.
   
   ```
   lsblk
   ```
   
   The column `MOUNTPOINT` shows where a block device is mounted. It's from this location that files on the disk can be accessed. 
   
   A first disk, sda, is also available, but it's not mounted. In this lab, you'll divide this disk into two partitions. You'll then mount one of these partitions onto the file system, so you can start accessing files from it.
   
   Optionally, view disks mounted on the system using the df command. This command is normally used to display the amount of space available on the file system. It lists all block devices with the available space on them. Use the -h option to display file sizes in human readable format.

    ```
    df -h
    ```
2. Partitions<br>
   IIt's common practice to divide a storage block into different partitions. Partitions can be different sizes, and formatted to different filesystems. This allows you to use a single storage device for different purposes.
   
   Display partition information using the `fdisk` command. You can also use the -l option to list partitions in the block. You can pass a device name to the `fdisk` command to list the partitions contained in that device. To list all partitions, use `fdisk -l`
   ```
   sudo fdisk -l PATH
   ```
   
   `fdisk` displays information contained in the partition table, where information about partitions is stored.

### Mount and umount

Mounting and unmounting mean making devices available or unavailable on a Linux file system. This is accomplished by the commands mount and umount. Before modifying a disk, first unmount it from the system, using the `umount` command. When modifications on the disk are done, mount it back onto the system.

Go ahead and start `fdisk` in interactive mode by passing the name of the disk.

```
sudo fdisk /dev/[SECOND DRIVE]
```

`fdisk` will start in interactive mode. 

* Use m to use help provided by the command
* Use p to show details about partitions on the disk
* Use q to exit interactive mode when you are finished exploring
* Use n to create a new partition
* Use d to delete the default partitions
* Use t to change the partition type
* Use q to quit fdisk without committing changes to the disk
* Use v to verify changes before proceeding
* Use w to commit changes to the disk

### Creating Partitions

1. Open fdisk in interactive mode to do the partitioning
   ```
   sudo fdisk /dev/[SECOND DRIVE]
   ```
   
   * If all the space on the disk is allocated, free up space by deleting the default partitions (Press `d`)
   * Create new partitions (Press `n`)
   * Enter the starting sector (memory location) of the new partition (Default 2048)
   * Enter the last sector of the new partition 
   
   The difference between the first and last sectors makes up the total size of the partition. Disk sector represents units used to measure the size on disks. Each sector stores a fixed amount of data. In lots of hard disks, for example, a sector stores 512 bytes. To create the first 1GB partition, enter 2097200 (divide the original partition by 10).
   
   * Enter t to change the partition type
   * L to view a list of all partition types
   * Enter w to commit changes

### Partitioning

1. Formatting partitions using `mkfs`<br>
   Multiple filesystem types exist, and it's important to know all of them, along with the functions they're best suited for.
   
   Format the second partition in unmounted drive to ext4:
   ```
   sudo mkfs -t ext4 /dev/[SECOND DRIVE]2
   ```
2. Mount<br>
   Mount second partition to a location on the file system to start accessing files on it.
   ```
   sudo mount /dev/[SECOND DRIVE]2 FILE-SYSTEM-LOCATION
   ```