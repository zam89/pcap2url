#!/usr/bin/env python
#
# pcap2url v0.2 (on 19 Feb 2017)
# Any issue/suggestion, please email to m[d0t]khairulazam[@]gmail[d0t]com

import sys
from scapy.all import *
from scapy.layers import http

try:
    import scapy.all as scapy
except ImportError:
    import scapy

f = open(sys.argv[1], "rb")
packets = scapy.rdpcap(f)

for p in packets:
	if p.haslayer("HTTPRequest"):
		ip_layer = p.getlayer('IP')
		http_layer = p.getlayer('HTTPRequest')
		print '\n{0[src]} just requested a {1[Method]} {1[Host]}{1[Path]}'.format(ip_layer.fields, http_layer.fields)
	if p.haslayer("HTTPResponse"):
		http_response = p.getlayer('HTTPResponse')
		print 'Response code {0[Status-Line]}'.format(http_response.fields)

print "\nDone. End of pcap"
