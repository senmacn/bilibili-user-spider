import random
def LoadUserAgents():
    uas = []
    with open('D:\\myPython\\project\\user_agents.txt','r') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip('\n').strip('"'))
    return uas

# 自行更换ip
proxies = [
    {'http':'http://112.195.158.164:808'},
    {'http':'http://223.198.111.242:53282'},
    {'http':'http://113.58.234.17:808'},
    {'http':'http://27.198.92.220:80'},
    {'http':'http://27.44.246.39:80'},
    {'http':'http://183.53.131.46:5853'},
    {'http':'http://106.42.23.167:808'},
    {'http':'http://219.157.246.179:8998'},
    {'http':'http://124.115.36.55:80'},
    {'http':'http://114.99.1.228:808'},
    {'http':'http://114.99.16.151:808'},
    {'http':'http://114.99.19.131:808'},
    {'http':'http://183.166.206.168:808'},
    {'http':'http://115.46.84.176:8123'},
    {'http':'http://221.229.18.200:3128'},
    {'http':'http://123.169.35.223:808,'},
    {'http':'http://113.124.92.178:808,'},
    {'http':'http://113.123.54.139:808,'},
    {'http':'http://123.55.88.7:808,'},
    {'http':'http://123.163.70.78:808,'}
            ]
