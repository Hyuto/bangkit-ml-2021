# Creating/inspecting key pair, encrypting/decrypting and sign/verify using OpenSSL

## Generating keys
1. Generating a private key<br>
   When someone wants to send data and make sure that no one else can view it, they can encrypt it with public key. Data that's encrypted with public key can only be decrypted with private key, to ensure that only you can view the original data. This is why it's important to keep private keys a secret! If someone else had a copy of private key, they'd be able to decrypt data that's meant for you. Not good!
   
   Generate a 2048-bit RSA private key
   ```
   openssl genrsa -out private_key.pem 2048
   ```
   
   The number of bits is specified with the last argument. The contents of the private key file should look like a large jumble of random characters.
2. Generating a public key<br>
   Generate the public key from the private key. You can give that to anyone who wants to send you encrypted data. When data is hashed using public key, nobody will be able to decrypt it unless they have your private key.
   
   ```
   openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem
   ```
   
3. Encrypting and decrypting<br>
   ```
   openssl rsautl -encrypt -pubin -inkey public_key.pem -in TEXT-FILE -out secret.enc
   ```
   
   The encrypted file will now be ready to send to whoever holds the matching private key. Remember that we must use the private key to decrypt the message, since it was encrypted using the public key. 
   ```
   openssl rsautl -decrypt -inkey private_key.pem -in secret.enc
   ```
4. Creating a hash digest<br>
   Create a hash digest of the message, then create a digital signature of this digest. Once that's done, you'll verify the signature of the digest. This allows you to ensure that your message wasn't modified or forged. If the message was modified, the hash would be different from the signed one, and the verification would fail.
   
   ```
   openssl dgst -sha256 -sign private_key.pem -out secret.txt.sha256 secret.txt
   ```
   
   With this file, anyone can use your public key and the hash digest to verify that the file hasn't been modified since you created and hashed it.
   
   **verification**
   
   ```
   openssl dgst -sha256 -verify public_key.pem -signature secret.txt.sha256 secret.txt
   ```