# coding=utf-8
import requests
import json
import constants
import testThread
def tx(url, mainAddress, hash, toAddress, fromAddress, fromAddressPri):
    reqParam = {
        "unionAccountAddress": mainAddress,
        "amount": "100000000000000000000",
        "relAddress": fromAddress,
        "relKey": fromAddressPri,
        "relTxHash": hash,
        "toAddress": toAddress
    }
    reqParam = json.dumps(reqParam)
    res = requests.post(url=url, data=reqParam)
    #print res.json()
    #return res.json()["hash"]


class MainCalls(object):
    def __init__(self):
        pass

    def userLogin(self, threadNum, url, pwd):
        # 开启多少个线程
        if (threadNum == 1):
            res = testThread.MyThread(url, pwd).run()
            grantToken = res['grantToken']
            return grantToken

        for num in range(0, threadNum):
            testThread.MyThread(url, pwd).start()

    def createAddress(self, url, grantToken):
        url = url + "/cks/wlt/pbcna.do"
        data = {"data": "{}", "busi": "zctest"}
        header = {"X-APP-AUTH": "{\"appId\":\"10000089\",\"busi\":\"zctest\"}", "GRANT-TOKEN": grantToken}
        data = json.dumps(data)
        res = requests.post(url=url, data=data, headers=header)
        #print res.json()
        return res.json()['addr']

    def chuangshikuaiTx(self, url, address):
        address1 = {"address": "34cef80a750b144ad258333f210f77a43186b14d",
                    "pri": "0bfff12774b4af6b2499142964de57dcd26b374a122da92c41ff4cdf279cc9d3"}
        address2 = {"address": "7f3a9aaa832196fc4b84d8997657d9977f3a93d4",
                    "pri": "0aaac4cceb1bbaf3add364e3a1a61bfee13b02a709eb65a68aedc5b0d39ed8ce"}
        address3 = {"address": "b750459bcc8b805f511dc04008541dacc554d5a2",
                    "pri": "be145f0c4afbc45f58a31eb67e0cd266e5feb0663d90942404b1d8e99417b219"}
        address4 = {"address": "806915cebbcfc95267b6bc221dce92fd5fb37107",
                    "pri": "34dc9befd347c01ec831e2296920cc9f0802a2c8278fcd97e4c2e82c9fea0b13"}
        address5 = {"address": "579b69b5b9bbfee0961fc59fb6bf36a0378f0150",
                    "pri": "02882ee7c12acc83a6aa66c818d4fd48076362ca821057c7343afb5bbca4ed93"}
        mainAddress = "bc317d01d7e0697f86fa50530b34241806ba4a2e"
        #address6 = {"address": "bc317d01d7e0697f86fa50530b34241806ba4a2e",
        #            "pri": "ab9cf6cb323b2038499ba425f682533603ec6768d890dc6804af7d972b04391a"}

        url = url+"/cks/tst/pbtua.do"
        tx(url=url,mainAddress=mainAddress,hash="",toAddress=address,fromAddress=address1["address"],fromAddressPri=address1["pri"])


if __name__ == '__main__':
    env = raw_input("请输入环境")
    dict = {"debug": constants.Constant().getDebugUrl(), "dev": constants.Constant().getDevUrl(), "test": constants.Constant().getTestUrl()}
    mainUrl = {"debug": constants.Constant().getDebugMainUrl(), "dev": constants.Constant().getDevMainUrl(),
               "test": constants.Constant().getTestMainUrl()}
    pwdDict = {"debug": '111111', "dev": '111111', "test": '123456'}
    a = dict.get(env)
    b = pwdDict.get(env)
    print a
    print b
    temp = MainCalls()
    # 用户登录
    grantToken = temp.userLogin(1, dict.get(env), pwdDict.get(env))
    # 创建地址
    # address = temp.createAddress(url=dict.get(env), grantToken=grantToken)
    # 从创始块里面充值
    #temp.chuangshikuaiTx(url=mainUrl.get(env), address=address)
