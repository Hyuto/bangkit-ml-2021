# Creating, Modifying, and Removing Files and Folders

**Graded Assessment : Lab (Qwiklab)**

### 1. Windows

Using GUI

### 2. Linux

1. Creating directories (folders)
    ```bash
    cd /home/user/Documents
    cat /home/user/Desktop/colors
    mkdir red blue green yellow magenta
    ```
2. Copying, moving and deleting files and directories (folders)
    ```bash
    cd /home/user/Pictures
    ls -a
    mv .apple .banana .broccoli .milk /home/user/Documents/Hidden
    ```
3. Searching in files
    ```bash
    grep -rw /home/user/Downloads -e "vacation"
    mv /home/user/Downloads/Iceland /home/user/Downloads/Japan /home/user/Documents
    ```
4. Editing files
    ```bash
    touch editor_test.txt
    nano editor_test.txt
    ```