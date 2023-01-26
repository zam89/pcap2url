#!/usr/bin/env python
#
# pcap2url v0.3 (on 25 Jan 2023)
# Any issue/suggestion, please email to m[d0t]khairulazam[@]gmail[d0t]com

import sys
import datetime
from scapy.all import *
from scapy.layers import http

try:
    import scapy.all as scapy
except ImportError:
    import scapy

f = open(sys.argv[1], "rb")
packets = scapy.rdpcap(f)

for p in packets:
    if "HTTPRequest" in p:
        ip_request = p["IP"]
        http_request = p["HTTPRequest"]
        #print(f'Raw {http_request.show()}')
        timestamp = datetime.utcfromtimestamp(int(p.time)).strftime('%Y-%m-%d %H:%M:%S UTC')
        print(f'\n{ip_request.src}:{ip_request.sport} requested {http_request.Method.decode()} {http_request.Host.decode()}{http_request.Path.decode()} at {timestamp} ({ip_request.dst}:{ip_request.dport})')
        if http_request.User_Agent:
            print(f'User_Agent: {http_request.User_Agent.decode()}')
        else:
            print("User_Agent: None")
        if http_request.Referer:
            print(f'Referer: {http_request.Referer.decode()}')
        else:
            print("Referer: None")
    if "HTTPResponse" in p:
        http_response = p["HTTPResponse"]
        #print(f'Raw {http_response.show()}')
        print(f'Response code: {http_response.Status_Code.decode()}')
        if http_response.Content_Disposition:
            print(f'Content_Disposition: {http_response.Content_Disposition.decode()}')
        else:
            print("Content_Disposition: None")
        print(f'Content_Type: {http_response.Content_Type.decode()}')

print("\nDone. End of pcap")
