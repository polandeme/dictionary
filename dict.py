import sys
import urllib
import urllib2
import json
arg = sys.argv[1]
argu = urllib2.quote(arg)

#terminal colors

GREEN = "\033[1;32m";
DEFAULT = "\033[0;49m";
BOLD = "\033[1m";
UNDERLINE = "\033[4m";
NORMAL = "\033[m";
RED = "\033[1;31m"

url = 'http://fanyi.youdao.com/openapi.do?keyfrom=ssssssq&key=1909161647&type=data&doctype=json&version=1.1&q=' + argu
reponse = urllib2.urlopen(url)
data = reponse.read()
tran = json.loads(data)
#print '-----------------------------------'
#print tran
trans = json.dumps(tran,ensure_ascii=False,)

bindex = trans.find('["') + 2
lindex = trans.find('"]')

bweb_trans = trans.find('explains":') + 13
lweb_trans =  trans.find(']}}') - 1

print RED + '\n-----------------------------------' + NORMAL
print NORMAL + trans[bindex:lindex]
print RED + '-----------------------------------'
print NORMAL + trans[bweb_trans:lweb_trans].replace(', "','\n')
print RED + '-----------------------------------\n' + NORMAL 


