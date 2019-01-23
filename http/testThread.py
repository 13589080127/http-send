import threading
import json
import requests


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        rootUrl = "http://172.16.211.13:38001/cks/wlt/pbusl.do"
        data = {"data": "{\"userName\":\"13589080127\",\"pwd\":\"123456\"}"}
        header = {"X-APP-AUTH": "{\"appId\":\"10000089\",\"busi\":\"zctest\"}"}
        print data
        data = json.dumps(data)
        print data
        res_data = requests.post(url=rootUrl, data=data, headers=header)
        print res_data.json()
