import urllib
from requests import post, get
from json import loads
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
users = {'15533356888': 'e31eff9cc5ee1e883a9cd541c70fac2b'}

class userLogin:
    def __init__(self, user_name):
        # 用户名
        self.user_name = user_name
        self.password = ''
        self.login_user = ''
        self.login_url = 'https://services2t.mvwchina.com/services'
        self.token = ''
        # 登录网站
        self.headers = {
            ':method': 'POST',
            ':path':'/services',
            ':authority': 'services2t.mvwchina.com',
            ':scheme': 'https',
            'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
            'accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'accept-encoding':'gzip, deflate, br',
            'referer':'https://yth.mvwchina.com/login.html',
            'content-type':'text/plain; charset=UTF-8',
            'origin':'https://yth.mvwchina.com'
        }
        # 跳转到考试系统登录
        self.headers_login2 = {
            ':method': 'POST',
            ':path': '/services2',
            ':authority': 'examup.mvwchina.com',
            ':scheme': 'https',
            'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0',
            'accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://exam.mvwchina.com/pc/student/teacher/admin.html?token=%s&fromyth=1',
            'content-type': 'text/plain; charset=UTF-8',
            'origin': 'https://exam.mvwchina.com'
        }
        self.data = ''
        if users.get(self.user_name):
            self.password = users[self.user_name]
        else:
            logging.error("%s:login failled,not find the user", self.user_name)
            sys.exit()

        # token
        pass

    # 获取登录信息，token
    def login(self):
        logging.info('start login....')
        json_data = {
                "terminalType": "A",
                "serviceModule": "UASService",
                "serviceNumber": "humanLogin",
                "token": "-1",
                "ip": "",
                "args": {"login": self.user_name, "pwd": self.password}
        }
        response = post(self.login_url, json=json_data)

        result = loads(urllib.parse.unquote(response.text))
        if result['serviceResult']['result']:
            self.token = result['serviceResult']['token']
            logging.info(self.token)
        else:
            logging.error("login failed:%s", result['serviceResult']['errorMessage'])
            sys.exit()

    def login2(self):
        data = {"serviceModule": "MVW-KAOSHINEW-T", "serviceNumber": "validateToken", "token": self.token,
                "args": {"token": self.token, "terminalType": "A"}, "terminalType": "A"}
        post(url='https://examup.mvwchina.com/services2', json=data)

    # 开始登陆
    def run(self):
        self.login()
        self.login2()


if __name__ == '__main__':
    logging.info("strat login")
    user = userLogin('15533356888')
    user.run()
