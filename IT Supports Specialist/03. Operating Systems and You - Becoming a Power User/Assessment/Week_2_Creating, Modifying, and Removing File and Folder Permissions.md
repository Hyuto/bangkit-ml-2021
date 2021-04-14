# Creating, Modifying, and Removing File and Folder Permissions

**Graded Assessment : Lab (Qwiklab)**

### 1. Windows

1. Example 1
   ```
   ICACLS C:\Users\Qwiklab\Documents\important_document
   ICACLS C:\Users\Qwiklab\Documents\important_document /remove "Kara"
   ICACLS C:\Users\Qwiklab\Documents\important_document /grant "Kara:(r)"
   ICACLS C:\Users\Qwiklab\Documents\important_document
   ```
2. Example 2
   ```
   ICACLS C:\Users\Qwiklab\Secret\
   ICACLS C:\Users\Qwiklab\Secret\ /grant "Phoebe:(r)"
   ICACLS C:\Users\Qwiklab\Secret\
   ICACLS C:\Users\Qwiklab\Secret\ /grant "Kara:(w)"
   ICACLS C:\Users\Qwiklab\Secret\
   ```
3. Example 3
   ```
   ICACLS C:\Users\Qwiklab\Music\
   ICACLS C:\Users\Qwiklab\Music\ /remove "Everyone"
   ICACLS C:\Users\Qwiklab\Music\ /grant "Everyone:(r)"
   ICACLS C:\Users\Qwiklab\Music\
   ```
4. Example 4
   ```
   ICACLS C:\Users\Qwiklab\Documents\not_so_important_document
   ICACLS C:\Users\Qwiklab\Documents\not_so_important_document /grant "Authenticated Users:(w)"
   ICACLS C:\Users\Qwiklab\Documents\not_so_important_document
   ```
5. Example 5
   ```
   ICACLS C:\Users\Qwiklab\Documents\public_document
   ICACLS C:\Users\Qwiklab\Documents\public_document /grant "Everyone:(r)"
   ICACLS C:\Users\Qwiklab\Documents\public_document
   ```

### 2. Linux

1. Changing file permissions
    ```
    cd ../qwiklab/documents
    sudo chmod 700 important_document
    ls -l important_document
    ```
2. Changing folder permissions
    ```
    cd ..
    ls -ld secret_folder/
    sudo chmod 720 secret_folder/
    ```
3. Changing owners
    ```
    sudo chown cook /home/qwiklab/taco
    ```
4. More practices
    ```
    sudo chmod u+x not_so_important_document
    sudo chmod g+w not_so_important_document
    sudo chmod a+r not_so_important_document
    sudo chmod 764 not_so_important_document
    ls -l not_so_important_document
    ```
5. Change permissions of not_so_important_document
    ```
    ls -l public_document
    sudo chmod a+rwx public_document
    sudo chmod 777 public_document
    ls -l public_document
    ```