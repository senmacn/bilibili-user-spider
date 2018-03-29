from project import agent
import threading
import requests,pymysql,json,time,random

headers = {'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'43',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'space.bilibili.com',
'Origin':'https://space.bilibili.com',
'Referer':'https://space.bilibili.com/2?spm_id_from=333.338.v_upinfo.2',
'User-Agent':'',
'X-Requested-With':'XMLHttpRequest'} #GetInfo-headers
headers2 = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'api.bilibili.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5006.400 QQBrowser/9.7.13101.400'} #api-headers
proxies = [
    {'http':'http://112.195.99.122:808'},
    {'http':'http://223.198.111.242:53282'},
    {'http':'http://112.66.215.136:808'},
    {'http':'http://27.198.92.220:80'},
    {'http':'http://27.44.246.39:80'},
    {'http':'http://183.53.131.46:5853'},
    {'http':'http://106.42.23.167:808'},
    {'http':'http://219.157.246.179:8998'}
            ]
formData = {'mid':1}
url = 'https://space.bilibili.com/ajax/member/GetInfo'
url1 = 'https://api.bilibili.com/x/relation/stat?'
agents = agent.LoadUserAgents()

def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time():
        return int(round(time.time() * 1000))
    return current_milli_time()

#爬虫程序
def spider(mid):
    lock.acquire()
    time.sleep(random.random())
    info = {'name': '', 'mid': 0, 'sex': '', 'level': 0, 'playnum': 0, 'regtime': '', 'follower': 0}

    #重组头文件，data文件
    theheaders = headers.copy()
    theheaders['User-Agent'] = random.choice(agents)
    theheaders2 = headers2.copy()
    theheaders2['User-Agent'] = random.choice(agents)
    Data = formData.copy()
    Data['mid'] = int(mid)

    #爬虫
    try:
        res = requests.session().post(url=url,data=Data, headers=theheaders,proxies=random.choice(proxies))
        jsinfo = json.loads(res.text, encoding='utf-8')
        if 'data' in jsinfo.keys():
            jsData = jsinfo['data']
            info['name'] = str(jsData['name'])
            info['mid'] = int(mid)
            info['sex'] = jsData['sex'] if 'sex' in jsData.keys() else 'nosex'
            info['level'] = jsData['level_info']['current_level']
            info['playnum'] = jsData['playNum']
            info['regtime'] = jsData['regtime']

            res2 = requests.session().get(url=url1,params={'vmid':mid,'jsonp':'jsonp'},headers=theheaders2,proxies=random.choice(proxies),timeout=2)
            js_fans_data = json.loads(res2.text)
            info['follower'] = js_fans_data['data']['follower']
            print('mid:%s获取' % (mid))
        else:
            print('no data now')

        #保存到数据库
        try:
            cur = db.cursor()
            cur.execute('insert INTO bilibili(name,mid,sex,level,playnum,regtime,follower) \
                            values("%s",%s,"%s",%s,%s,%s,%s)'
                            % (info['name'],info['mid'],info['sex'],info['level'],info['playnum'],info['regtime'],info['follower']))
            db.commit()
            cur.close()
            print('mid:%s 保存成功'%(mid))
        except:
            print('%s:保存失败'%(mid))
    except:pass
    lock.release()

if __name__ == '__main__':
    # 连接数据库
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='mypydb')
    lock = threading.Lock()
    for i in range(0,10000):
        try:
            threads = [threading.Thread(target=spider,args=(20*i+j,)) for j in range(1,21)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
        except:pass
        time.sleep(8)
    db.close()