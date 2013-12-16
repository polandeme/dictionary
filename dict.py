import sys
import urllib
import urllib2
import json
arg = sys.argv[1]
argu = urllib2.quote(arg)
url = 'http://fanyi.youdao.com/openapi.do?keyfrom=ssssssq&key=1909161647&type=data&doctype=json&version=1.1&q=' + argu
reponse = urllib2.urlopen(url)
data = reponse.read()
tran = json.loads(data)
#print '-----------------------------------'
#print tran
trans = json.dumps(tran,ensure_ascii=False,)
#print trans
bindex = trans.find('["') + 2
lindex = trans.find('"]')
print '-----------------------------------'
print trans[bindex:lindex]
print '-----------------------------------'
