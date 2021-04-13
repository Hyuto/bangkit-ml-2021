# The Bits and Bytes of Computer Networking

## Materi

* Week 1<br>
   1. Introduction to Computer Networking
   2. The TCP/IP Five-Layer Network Model
   3. The Basics of Networking Devices
   4. The Physical Layer
   5. The Data Link Layer
   
   **Note**

   1. OSI Networking Model : [link 1](https://www.sans.org/reading-room/whitepapers/standards/osi-model-overview-543) & [link 2](https://en.wikipedia.org/wiki/OSI_model)
   2. [Ethernet Over Twisted Pair Technologies](https://en.wikipedia.org/wiki/Ethernet_over_twisted_pair)

   **Assessment**

   1. [Layers in Networking Models](Assessment/Week_1_01%20Layers%20in%20Networking%20Models.md)
   2. [Networking Basics](Assessment/Week_1_02%20Networking%20Basic.md)
* Week 2<br>
   1. The Network Layer
   2. Subnetting
   3. Routing
   
   **Note**

   1. Routing Protocol<br>
      * [Internet Engineering Task Force (IETF)](https://www.ietf.org/)
      * Distance vector protocols 
        * [Routing Information Protocol (RIP)](https://en.wikipedia.org/wiki/Routing_Information_Protocol) ([IETF RFC2453](https://tools.ietf.org/html/rfc2453))
        * [Enhanced Interior Gateway Routing Protocol (EIGRP)](https://en.wikipedia.org/wiki/Enhanced_Interior_Gateway_Routing_Protocol) ([Cisco documentation](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)). 
      * Link state protocol 
        * [Open Shortest Path First (OSPF)](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) ([IETF RFC2328](https://tools.ietf.org/html/rfc2328)).
       * Gateway protocols
         * [Border Gateway Protocol (BGP)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) ([IETF RFC4271](https://tools.ietf.org/html/rfc4271)).
   2. RFCs and Standards<br>
   RFCs have come to belong to the Internet [Engineering Task Force (IETF)](https://www.ietf.org/), which is an open community charged with developing and maintaining the standards required for the Internet to continue to operate. [Large collections of RFCs](https://www.ietf.org/standards/rfcs/)

   **Assessment**

   1. [Routing Paths and Subnets](Assessment/Week_2_01%20Routing%20Paths%20and%20Subnets.md)
   2. [Network Layer](Assessment/Week_2_02%20The%20Network%20Layer.md)
* Week 3<br>
   1. Introduction to the Transport and Application Layers
   2. The Transport Layer
   3. The Application Layer
   
   **Note**

   1. [System Ports vs Ephemeral Ports](Assets/System%20Ports%20vs%20Ephemeral%20Ports.md)

   **Assessment** : [The Transport and Application Layer](Assessment/Week_3_01%20The%20Transport%20and%20Application%20Layer.md)
* Week 4<br>
   1. Introduction to Network Services
   2. Name Resolution
   3. Name Resolution in Practice
   4. Dynamic Host Configuration Protocol
   5. Network Address Translation
   6. VPNs and Proxies

   **Note**

   1. [IPv4 Address Exhaustion](Assets/IPv4%20Address%20Exhaustion.md)

   **Assessment**

   1. [Networking Services Simulation](Assessment/Week_4_01%20Networking%20Services%20Simulation.md)
   2. [Networking Services](Assessment/Week_4_02%20Networking%20Services.md)
* Week 5<br>
   1. Introduction to Connecting to the Internet
   2. POTS and Dial-up
   3. Broadband Connections
   4. WANs
   5. Wireless Networking
   
   **Note**

   1. Broadband Protocols<br>
   Internet connections used to require very careful setup, configuration and monitoring. Today, an Internet connection is mostly a working service provided by an ISP that doesn’t require much maintenance by those that use it.
   2. WAN Protocols<br>
   It’s important to note that these protocols usually define how both the physical and data link layers need to operate when they’re deployed.
      * [Frame Relay](https://en.wikipedia.org/wiki/Frame_Relay)
      * [High-Level Data Link Control (HDLC)](https://en.wikipedia.org/wiki/High-Level_Data_Link_Control)
      * [Asynchronous Transfer Mode (ATM)](https://en.wikipedia.org/wiki/Asynchronous_Transfer_Mode)
   3. [Mobile Device Networks](Assets/Mobile%20Device%20Networking.md)
  
    **Assessment** 

    1. [Wireless Channels](Assessment/Week_5_01%20Wireless%20Channels.md)
    2. [Connecting to The Internet](Assessment/Week_5_02%20Connecting%20to%20The%20Internet.md)
* Week 6<br>
    1. Introduction to Troubleshooting and the Future of Networking
    2. Verifying Connectivity
    3. Digging into DNS
    4. The Cloud
    5. IPv6
    
    **Note**

    1. Testing Port Connectivity :  [Netcat (nc)](https://en.wikipedia.org/wiki/Netcat) on Linux and macOS, and [Test-NetConnection](https://docs.microsoft.com/powershell/module/nettcpip/test-netconnection) on Windows.
    
    **Assessment**

    1. [IPv6 Compression](Assessment/Week_6_01%20IPv6%20Compression.md)
    2. [Troubleshooting and the Future of Networking](Assessment/Week_6_02%20Troubleshooting%20and%20the%20Future%20of%20Networking.md)