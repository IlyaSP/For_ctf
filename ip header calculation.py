# -*- coding: utf-8 -*-
from scapy.layers.inet import IP

checksum = '0xf921'
# длина ip заголовка, берётся из wireshrk или аналогов
# length of ip header, taken from wireshrk or analogs
len_ip_head = 60

for i in range(0, 255, 1):
    for ii in range(0, 255):
        dst = '95.211.{0}.{1}'.format(i, ii)   # ip address generation
        # Все параметры для генерации беруться из wireshark или аналогов
        # All parameters for generation are taken from wireshark or analogues
        pak = IP(dst=dst, src="10.0.2.15", ttl=64, flags="DF", id=28368, len=len_ip_head + 6, chksum=0)
        del pak[IP].chksum    # delete checksum from head
        pkt1 = IP(raw(pak))   # generate ip head with checksum
        cur_checksum = hex(pkt1[IP].chksum)
        if cur_checksum == checksum:
            print(dst)
            print(pkt1.show())   # detailed package output 
            break
        else:
            continue
