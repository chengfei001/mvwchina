import urllib

from requests import request,post
from json import loads
import logging
import sys
logging.basicConfig(level=logging.DEBUG)


users = {'15533356888': 'e31eff9cc5ee1e883a9cd541c70fac2b'}

class userLogin:
    def __init__(self, username):
        self.username =username
        #获取md5加密后的密码
        self.password = ''

        if users.get(self.username):
            self.password = users[username]
        else:
            logging.info('用户不在可抓取列表中')
            sys.exti()

        self.token = ''
        self.url_login = 'https://services2t.mvwchina.com/services'
        self.headers = {
            ':method':'POST',
            ':path':'/services',
            ':authority':'services2t.mvwchina.com',
            ':scheme':'https',
            'user-agent':'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
            'accept':'*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'accept-encoding':'gzip, deflate, br',
            'referer':'https://yth.mvwchina.com/login.html',
            'content-type':'text/plain; charset=UTF-8',
            'origin':'https://yth.mvwchina.com'
        }

        self.headers2 = {
            ':method': 'POST',
            ':path': '/services2',
            ':authority': 'examup.mvwchina.com',
            ':scheme': 'https',
            'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
            'accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://exam.mvwchina.com/pc/student/teacher/admin.html?token=8af87cffd63e4013b53e4e53f5f35c0a&fromyth=1',
            'content-type': 'text/plain; charset=UTF-8',
            'origin': 'https://exam.mvwchina.com'
        }



    def login(self):
        # logging.info('start login....')
        # # "terminalType":"A","serviceModule":"UASService","serviceNumber":"humanLogin","token":"-1","args":{"login":"15533356888","pwd":"e31eff9cc5ee1e883a9cd541c70fac2b"},"ip":""
        # data = {
        #         "terminalType": "A",
        #         "serviceModule": "UASService",
        #         "serviceNumber": "humanLogin",
        #         "token": "-1",
        #         "ip": "",
        #         "args": {"login":"15533356888","pwd":"e31eff9cc5ee1e883a9cd541c70fac2b"}
        # }
        # # print(data)data
        # # response = post(url=self.url_login, json=data)
        # # print(response.text)
        # # print(urllib.parse.unquote(response.text))
        # response = post(url='https://exam.mvwchina.com/pc/student/teacher/admin.html?token=95c38783e1ce4cda8ef4aca6d0fbc344')
        # result = loads(urllib.parse.unquote(response.text))
        #
        # if result['errorMessage']== 'null':
        #     self.token = result['serviceResult']['token']
        #     logging.info('loggin success...')
        #
        # logging.info('end loggin...')

        data = {"serviceModule": "MVW-KAOSHINEW-T", "serviceNumber": "10201300",
                "token": "8af87cffd63e4013b53e4e53f5f35c0a",
                "args": {"bankId": "99c6784a9a8611e69446fcaa14579e1e", "keywordId1": "6fd29f571fea4a208bc8a72db1639fd0",
                         "keywordId2": "null", "keywordId3": "null", "keywordId4": "null", "keywordId5": "null",
                         "classifyType": "null", "questionTypeCode": "null", "difficulty": "null",
                         "havePictures": "null", "haveAnalyse": "null", "topic": "null", "remarks": "null",
                         "auditingStatus": "null", "pages": 1, "maxNum": 20}, "terminalType": "A"}
        logging.info("get page")
        response = post(url='https://examup.mvwchina.com/services2', json=data)
        print(urllib.parse.unquote(response.text))




    def run(self):
        self.login()
if __name__ == '__main__':
    logging.info("aa")
    user = userLogin('15533356888')
    user.run()

