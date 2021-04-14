# Creating, Modifying, and Removing File and Folder Permissions

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
    ls -l FILE
    ```
2. Changing file permissions
    ```
    sudo chmod 700 FILE
    ls -l FILE
    ```
3. Changing folder permissions
    ```
    ls -ld FOLDER/
    ```
    
    To add execute to the owner's permission, you can use the command below. (Note that "u" stands for "user" and "x" stands for "execute".)
    
    ```
    sudo chmod u+x FOLDER/
    ```

    Fix the group's permission. "g" stands for "group" (like "u" from before), and "w" and "r" stand for "write" and "read" respectively:

    ```
    sudo chmod g+w FOLDER/
    sudo chmod g-r FOLDER/
    ```
    
    Finally, you can remove read permissions from everyone else using the command below ("o" stands for "other"):

    ```
    sudo chmod o-r FOLDER/
    ```
    
    All the previous steps could also have been done using the numerical notation, like this:

    ```
    sudo chmod 720 FOLDER/
    ```
4. Changing owners<br>
    There's another user account on the machine called "cook". Go ahead and make "cook" the owner of the file, using the chown command like this:

    ```
    sudo chown cook FILE
    ```