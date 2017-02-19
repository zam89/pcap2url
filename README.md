# pcap2url
Extracting URLs from PCAP file

![alt tag](https://raw.githubusercontent.com/zam89/pcap2url/master/screenshot.jpg)

<h1>About</h1>
<p>This system basically extracting URLs inside PCAP file into more human-friendly and beautiful format. :p</p>
<p>This is just a layman's coding style. Create this just for fun and for learning purpose.</p>

<p><h1>Main Function</h1></p>
<li>This analyzer will read the PCAP file and display the result in the terminal.</li><br>
The result will contains:
<ul>
  <li>Source IP</li>
  <li>HTTP Method</li>
  <li>Requested URL</li>
  <li>HTTP Response</li>
</ul>

<h1>How to use</h1>
<ol>
  <li>Clone/download this code</li>
  <li>Install Python2.7 (currently I'm running Python 2.7.10)</li>
  <li>Install pip module</li>
  <li>Install scapy, scapy-http via pip -e.g. pip install scapy scapy-http</li>
  <li>Download "__init__.py" to "C:\Python27\Lib\site-packages\scapy\arch\windows"</li>
  <li>Run this code: python pcap2url.py file-sample.pcap</li>
  <li>Profit! :)</li>
</ol>

<li>Any feedback are welcomed. You can contact me via email at <b>m[d0t]khairulazam@gmail[d0t]com</b>.</li>

<li>Credit for this <a href="http://snippets1000.blogspot.my/2012/09/scapy-and-http.html">blog</a> for the original code. :)</li>
