# Creating, Modifying, and Removing File and Folder Permissions

**Graded Assessment : Lab (Qwiklab)**

### 1. Windows

Using : Powershell

1. Check file permission
    ```
    ICACLS {FILE_PATH}
    ```
2. Remove from the file's permissions
    ```
    ICACLS {FILE_PATH} /remove "{NAME}"
    ```
3. Grant permission
    ```
    ICACLS {FILE_PATH} /grant "{NAME}:({TYPE})"
    ```

    **Types**

    * r : Read Only
    * w : Write

### 2. Linux

1. Checking permissions
    ```
    ls -l important_document
    ```
2. Changing file permissions
    ```
    sudo chmod 700 important_document
    ls -l important_document
    ```
3. Changing folder permissions
    ```
    ls -ld secret_folder/
    ```
    
    To add execute to the owner's permission, you can use the command below. (Note that "u" stands for "user" and "x" stands for "execute".)
    
    ```
    sudo chmod u+x secret_folder/
    ```

    Fix the group's permission. "g" stands for "group" (like "u" from before), and "w" and "r" stand for "write" and "read" respectively:

    ```
    sudo chmod g+w secret_folder/
    sudo chmod g-r secret_folder/
    ```
    
    Finally, you can remove read permissions from everyone else using the command below ("o" stands for "other"):

    ```
    sudo chmod o-r secret_folder/
    ```
    
    All the previous steps could also have been done using the numerical notation, like this:

    ```
    sudo chmod 720 secret_folder/
    ```
4. Changing owners
    There's another user account on the machine called "cook". Go ahead and make "cook" the owner of the file, using the chown command like this:

    ```
    sudo chown cook /home/qwiklab/taco
    ```
5. More practices
    ```
    sudo chmod u+x not_so_important_document
    ls -l not_so_important_document
    sudo chmod g+w not_so_important_document
    ls -l not_so_important_document
    sudo chmod a+r not_so_important_document
    ls -l not_so_important_document
    sudo chmod 764 not_so_important_document
    ```
6. Change permissions of not_so_important_document
    ```
    ls -l public_document
    sudo chmod a+rwx public_document
    ls -l public_document
    sudo chmod 777 public_document
    ```
