import httplib

conn = httplib.HTTPConnection('localhost:8383')
conn.request('GET', '/?test_scenario=c:/dev/python/bdd/features/google_search.feature')
resp = conn.getresponse()
data = resp.read()
print "***DATA***\n"
print data