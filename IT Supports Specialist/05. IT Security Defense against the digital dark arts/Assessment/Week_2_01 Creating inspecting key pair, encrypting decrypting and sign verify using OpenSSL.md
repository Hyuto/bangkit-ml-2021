# Creating/inspecting key pair, encrypting/decrypting and sign/verify using OpenSSL

**Graded Assessment : Lab (Qwiklab)**

1. Generating keys<br>
   * Generating a private key
    ```
    openssl genrsa -out private_key.pem 2048
    cat private_key.pem
    ```
   * Generating a public key
    ```
    openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
    cat public_key.pem
    ```
2. Encrypting and decrypting
   ```
   echo 'This is very secret message' > secret.txt
   openssl rsautl -encrypt -pubin -inkey public_key.pem -in secret.txt -out secret.enc
   openssl rsautl -decrypt -inkey private_key.pem -in secret.enc
   ```
3. Creating a hash digest
   ```
   openssl dgst -sha256 -sign private_key.pem -out secret.txt.sha256 secret.txt
   openssl dgst -sha256 -verify public_key.pem -signature secret.txt.sha256 secret.txt
   ```