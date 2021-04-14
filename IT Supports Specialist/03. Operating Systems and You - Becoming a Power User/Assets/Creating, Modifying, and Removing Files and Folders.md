# Creating, Modifying, and Removing Files and Folders

1. Creating directories (folders)
    ```
    mkdir dir1 dir2 dir3
    ```
    **Parameters**

    `mkdir` can take three options:

    * -p: allow mkdir to create parent directories if they don't exist
    * -m: (mode) used to set permissions of directories during creation
    * -v: run command in verbose mode
    * Let's take a look at how to use mkdir by going through an example.
2. Removing empty directories
    ```bash
    rmdir dir_name
    rmdir dir1 dir2 dir3 dir4
    ```
    
    `rmdir` only removes empty directories
    
    **Options**

    * -p: remove parent directories, if they're also empty
3. Creating files
    ```bash
    touch empty_file
    ```
    
    **Options**

    * -c: do not create file if it doesn't exist
4. Copying, moving and deleting files and directories (folders)
    ```bash
    cp /home/user/source_file /home/user/duplicates/target_file
    mv /home/user/source_file /home/user/moved_files/target_file
    rm /home/user/duplicates/target_file
    ```
5. Move hidden files
    ```bash
    mv /home/user/Movies/Europe\ Pictures /home/user/Pictures
    cd /home/user/Pictures
    mv /home/user/Images/Vacation.JPG .
    ```
6. Move files and folders
    ```bash
    cd /home/user/Music
    rm Best_of_the_90s 80s_jams Classical
    rmdir Rock
    ```
7. Remove files and folders
    ```bash
    rm -r non_empty_dir
    ```
8. Searching in files
    ```bash
    grep
    ```

    **Options and flags**

    -r: search recursively
    -w: match the whole word
    -n: only in line number
    -e: match pattern
    --include and --exclude: include and exclude files in the search
    --include-dir and --exclude-dir: include or exclude directories in the search

    **Code**
    
    ```bash
    grep -rw /home/user/Downloads -e "vacation"
    mv /home/user/Downloads/Iceland /home/user/Downloads/Japan /home/user/Documents
    ```
9. Editing files
    ```bash
    nano /path/to/existing/file
    ```
    
    **Keybinds**

    * To save modifications to the file, use CTRL-O
    * Once editing is done, we can close and exit the program using CTRL-X
    * Get help using CTRL-G
    
    **Code**

    ```bash
    touch editor_test.txt
    nano editor_test.txt
    ```