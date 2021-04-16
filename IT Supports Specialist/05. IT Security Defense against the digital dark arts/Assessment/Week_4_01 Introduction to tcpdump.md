# Introduction to `tcpdump`

**Graded Assessment : Lab (Qwiklab)**

1. Saving Captured Packets
   ```
   sudo tcpdump -i eth0 port 80 -w http.pcap &
   [enter]
   jobs -l
   curl example.com
   fg % [job-id]
   tcpdump -r http.pcap -nv
   ```