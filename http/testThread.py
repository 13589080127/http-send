import json
import threading
import time
from decimal import Decimal

import requests


class MyThread(threading.Thread):
    def __init__(self, url, pwd):
        threading.Thread.__init__(self)
        self.url = url
        self.pwd = pwd

    def run(self):
        rootUrl = self.url+"/cks/wlt/pbusl.do"
        data = {"data": "{\"userName\":\"13589080127\",\"pwd\":\""+self.pwd+"\"}"}
        header = {"X-APP-AUTH": "{\"appId\":\"10000089\",\"busi\":\"zctest\"}"}
        data = json.dumps(data)
        print data
        time1 = time.time()*100
        res_data = requests.post(url=rootUrl, data=data, headers=header)
        print round(Decimal((time.time()*100)-time1),0)
        print res_data.json()
        return res_data.json()
