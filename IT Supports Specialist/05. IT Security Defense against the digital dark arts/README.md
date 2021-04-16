# IT Security: Defense against the digital dark arts

## Materi

* Week 1<br>
  1. Introduction to IT Security
  2. Malicious Software
  3. Network Attacks
  4. Other Attacks
   
   **Note**

   1. [Malicious Software](http://www.independent.co.uk/news/business/news/disgruntled-worker-tried-to-cripple-ubs-in-protest-over-32000-bonus-481515.html)
   2. [Network Attacks](https://threatpost.com/major-dns-cache-poisoning-attack-hits-brazilian-isps-110711/75859/)
   3. [DDoS Attacks](https://en.wikipedia.org/wiki/2016_Dyn_cyberattack)
   
   **Assessment** : [Understanding Security Threats](Assessment/Week_1_01%20Understanding%20Security%20Threats.md)
* Week 2<br>
  1. Symmetric Encryption
  2. Public Key or Asymmetric Encryption
  3. Hashing
  4. Cryptography Applications
   
   **Note**

   1. [The Future of Cryptanalysis](Assets/The%20Future%20of%20Cryptanalysis.md)
   2. [Symmetric Encryptions](http://www.rc4nomore.com/)
   3. [Asymmetric Encryption Attack](Assets/Asymmetric%20Encryption%20Attack.md)
   4. SHA1 Attacks<br>
   During the 2000s, a bunch of theoretical attacks against SHA1 were formulated and some partial collisions were demonstrated. In early 2017, the first full collision of SHA1 was published.
   1. [X.509 Standard](https://www.ietf.org/rfc/rfc5280.txt)
   2. [PGP](http://www.philzimmermann.com/EN/essays/WhyIWrotePGP.html) : developed by Phil Zimmermann in 1991 and was freely available for anyone to use
   3. Securing Network Traffic
   4. [TPM Attacks](https://gcn.com/Articles/2010/02/02/Black-Hat-chip-crack-020210.aspx)
   5. [Note : Creating/inspecting key pair, encrypting/decrypting and sign/verify using OpenSSL](Assets/Creating%20inspecting%20key%20pair,%20encrypting%20decrypting%20and%20sign%20verify%20using%20OpenSSL.md)

   **Assessment**

   1. [Creating/inspecting key pair, encrypting/decrypting and sign/verify using OpenSSL](Assessment/Week_2_01%20Creating%20inspecting%20key%20pair,%20encrypting%20decrypting%20and%20sign%20verify%20using%20OpenSSL.md)
   2. [Hands-on with Hashing](Assessment/Week_2_02%20Hands-on%20with%20Hashing.md)
* Week 3<br>
  1. Authentication
  2. Authorization
  3. Accounting
   
   **Note**

   1. [Creating fake fingerprints using things like glue](http://www.planetbiometrics.com/article-details/i/5774/desc/indian-pupils-cheat-biometric-system-with-glue/)
   2. [OAuth-based worm-like attack](https://www.theverge.com/2017/5/3/15534768/google-docs-phishing-attack-share-this-document-with-you-spam)
   

   **Assessment** : [AAA Security (Not Roadside Assistance)](Assessment/Week_3_01%20AAA%20Security.md)
* Week 4<br>
  1. Secure Network Architecture
  2. Wireless Security
  3. Network Monitoring
   
   **Note**

   1. Network Hardening Best Practices
      * [Cisco IOS firewall rules](https://www.cisco.com/en/US/docs/routers/access/800/850/software/configuration/guide/firewall.html)
      * [Juniper firewall rules](https://www.juniper.net/documentation/en_US/junos/topics/usage-guidelines/services-configuring-stateful-firewall-rules.html)
      * [Iptables firewall rules](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
      * [UFW firewall rules](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
      * [Configuring Mac OS X firewall](https://support.apple.com/en-us/HT201642)
      * [Microsoft firewall rules](https://technet.microsoft.com/en-us/library/cc754274(v=ws.11).aspx)
   2. [IEEE 802.1X](https://en.wikipedia.org/wiki/IEEE_802.1X)
   3. HAProxy, nginx and Apache HTTP server
      * [HAProxy main documentation](http://www.haproxy.org/#docs)
      * [HAProxy reverse proxy documentation](http://cbonte.github.io/haproxy-dconv/1.8/intro.html#3.3.1)
      * [nginx main documentation](http://nginx.org/en/docs/)
      * [nginx reverse proxy documentation](http://nginx.org/en/docs/beginners_guide.html#proxy)
      * [Apache HTTP server main documentation](http://httpd.apache.org/docs/)
      * [Apache HTTP server reverse proxy documentation](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html)
   4. [WEP Encryption and Why You Shouldn't Use It](https://doi.org/10.1007/3-540-45537-X_1)
   5. [WiFi Protected Setup (WPS) PIN brute force vulnerability](https://www.kb.cert.org/vuls/id/723755)
   
   **Assessment** : [Introduction to `tcpdump`](Assessment/Week_4_01%20Introduction%20to%20tcpdump.md)
* Week 5<br>
  1. System Hardening
  2. Application Hardening
   
   **Note**

   1. [Logging and Auditing](https://github.com/rsyslog/rsyslog)
   2. Disk Ecryption
      * Full Disk Encryption : [BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) & [FileVault 2](https://support.apple.com/en-us/HT204837)
      * Open-Source Solution : [dm-crypt package](https://wiki.archlinux.org/index.php/dm-crypt)
   
   **Assessment** : [Defense in Depth](Assessment/Week_5_01%20Defense%20in%20Depth.md)
* Week 6<br>
  1. Risk in the Workplace
  2. Users
  3. Incident Handling
   
   **Note**

   1. Risk in the Workplace : [Nessus](https://www.tenable.com/products/nessus-vulnerability-scanner), [OpenVAS](http://www.openvas.org/), and [Qualys](https://www.qualys.com/forms/freescan/)
   2. [Password Alert](https://support.google.com/a/answer/6197508?hl=en)
   3. [Vendor Security Assessment Questionnaires](https://vsaq-demo.withgoogle.com/)
   
   **Assessment** : [Creating a Company Culture for Security](Assessment/Week_6_01%20Creating%20a%20Company%20Culture%20for%20Security.md)