
# here urllib.parse is module and urlparse is method name
from urllib.parse import urlparse
a = urlparse('http://www.bsr.com:9999')

print(a.hostname)

print(a.port)
