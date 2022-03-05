from urllib.request import urlopen
import json
import requests

ip = json.load(urlopen('http://httpbin.org/ip'))['origin']
print("获取公网IP："+ip)

#curl -X POST https://dnsapi.cn/Record.Ddns -d 'login_token=LOGIN_TOKEN&format=json&domain_id=2317346&record_id=16894439&record_line_id=10%3D0&sub_domain=www'
#curl -X POST https://dnsapi.cn/Record.Modify -d 'login_token=****,*************************&format=json&domain_id=2317346&record_id=16894439&sub_domain=www&value=3.2.2.2&record_type=A&record_line_id=10%3D0'
urlinfo="https://dnsapi.cn/Record.Info"
headers = {'User-Agent': 'xmghocom dnspod Client/1.0.0(admin@xmgho.com)'}
datainfo={
'login_token':'****,*************************',
'format':'json',
'domain_id':'19665460',
'record_id':'694052900',
}
urldone="https://dnsapi.cn/Record.Modify"

datadone={
'login_token':'****,*************************',
'format':'json',
'domain_id':'19665460',
'record_id':'694052900',
'sub_domain':'vip',
'value':ip,
'record_type':'A',
'record_line_id':'0',
'ttl ':'10',
}
#'login_token': '****,*************************',
response = requests.post(urlinfo, headers=headers,data=datainfo)
urldata = json.loads(response.text)
#print(urldata)
vipip=urldata['record']['value']
print("记录值IP："+vipip)
if ip==vipip:
    print("获取公网IP=记录值IP,无需更新!")
else:
    responsedone = requests.post(urldone, headers=headers, data=datadone)
    data = json.loads(responsedone.text)
    #print(data)
    vipnew = data['record']['value']
    doneinfo = data['status']['message']
    print(doneinfo+":"+vipnew)
