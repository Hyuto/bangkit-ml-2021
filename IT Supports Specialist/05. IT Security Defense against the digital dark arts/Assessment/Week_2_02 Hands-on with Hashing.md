# Hands-on with Hashing

**Graded Assessment : Lab (Qwiklab)**

1. MD5
   ```
   echo 'This is some text in a file, just so we have some data' > file.txt
   md5sum file.txt > file.txt.md5
   md5sum -c file.txt.md5
   ```
2. Verifying an invalid file
   ```
   cp file.txt badfile.txt
   md5sum badfile.txt > badfile.txt.md5
   nano badfile.txt
   md5sum -c badfile.txt.md5
   md5sum badfile.txt > new.badfile.txt.md5
   cat new.badfile.txt.md5
   ```
3. SHA1
   ```
   shasum file.txt > file.txt.sha1
   cat file.txt.sha1
   shasum -c file.txt.sha1
   ```
4. SHA256
   ```
   shasum -a 256 file.txt > file.txt.sha256
   cat file.txt.sha256
   shasum -c file.txt.sha256
   ```