import logging
import sys
from requests import request, post
from json import loads, dumps

from login import userLogin
import urllib

logging.basicConfig( level = logging.INFO)

class GetQuestion:
    def __init__(self):
        self.url_question = 'https://examup.mvwchina.com/services2'
        self.user = userLogin('15533356888')
        self.headers_question_10201300 = {
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
        logging.info("bbb")

        pass

    # 获取考试页面
    def get_question(self):
        # "keywordId1": null, "keywordId2": null,
        # "keywordId3": null, "keywordId4": null, "keywordId5": null, "classifyType": null,
        # "questionTypeCode": null,
        # "difficulty": null, "havePictures": null, "haveAnalyse": null, "topic": null, "remarks": null,
        # "auditingStatus": null,
        # bankId 可调整 pages根据情况修改翻页 servciecNuber是服务的编码
        data = {"serviceModule": "MVW-KAOSHINEW-T", "serviceNumber": "10201300", "token": "%s",
                "args": {"bankId": "99c676979a8611e69446fcaa14579e1e",
                         "pages": 1, "maxNum": 20}, "terminalType": "A"}
        data["token"] = self.user.token
        response = post(user.url_question, json=data)

        logging.info(urllib.parse.unquote(response.text))
        pass


    # 运行获取页面
    def run(self):
        self.get_question()
        pass


if __name__ == '__main__':
    question = GetQuestion()
    question.run()