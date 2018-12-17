import logging
from requests import request, post
from json import loads, dumps

from login import userLogin
import urllib

from pymongo import MongoClient
import time
import random

logging.basicConfig(level=logging.INFO)


client = MongoClient('mongodb://localhost:27017')
db = client['yth_mvwchina']



class GetQuestion:
    def __init__(self):
        self.url_question = 'https://examup.mvwchina.com/services2'
        self.user = userLogin('15533356888')
        self.user.run()
        # self.user.token = '035e0136990d45898a2adee613bb8d43'
        # 每页取max_num条数据
        self.max_num = 500
        # 题库id
        # self.bankId = '99c676979a8611e69446fcaa14579e1e'  #职业医师
        self.bankIds = {'99c6784a9a8611e69446fcaa14579e1e','99c676979a8611e69446fcaa14579e1e'}  #住陪考核
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

    # 获取考试页面
    def get_question(self, pages, max_num, bankId):
        # bankId 可调整 pages根据情况修改翻页 servciecNuber是服务的编码
        data = {"serviceModule": "MVW-KAOSHINEW-T", "serviceNumber": "10201300",
                "token": self.user.token, "args": {"bankId": bankId,
                                                   "pages": pages,
                                                   "maxNum": max_num}, "terminalType": "A"}
        # logging.info("get page")
        response = post(url='https://examup.mvwchina.com/services2', json=data)
        # 获取数据结果转换成dict
        result = loads(loads(urllib.parse.unquote(response.text))["serviceResult"])
        # 获取数据总条目
        total_size = result['totalSize']
        return (total_size, result)




    #处理页面内容并保存
    def question_analysis_save(self, result):

        # 获取数据,将questions和question_details全部保存到MongoDB中
        question_details = result['questionDetails']
        questions = result['questions']
        # logging.info('questionDetails：：：：：：'+question_details)

        # logging.info('questions：：：：：：：'+questions)
        db['questions_details'].insert_many(question_details)

        db['questions'].insert_many(questions)

        # 处理图片
        # 处理分析子题 分析子题功能甲方暂不需要
        # 保存试题到MongoDB
        return


    # 运行获取页面
    def run(self):
        '''
        # 参数第几页 一页去几条   大类
        self.get_question(1,20,'99c676979a8611e69446fcaa14579e1e')
        '''

        '''循环题库'''
        for bankId in self.bankIds:
            (total_size, result) = self.get_question(1, self.max_num, bankId)
            page_count = int(total_size/self.max_num+1)
            logging.info(bankId)
            i = 1
            '''循环获取页面功能代码'''
            while i <= page_count:
                logging.info(i)
                (total_size, result) = self.get_question(i, self.max_num, bankId)
                self.question_analysis_save(result)
                time.sleep(random.randint(2, 7))
                i += 1



if __name__ == '__main__':
    question = GetQuestion()
    question.run()

