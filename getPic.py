import os
from requests import get

import os
import re
import logging
from pymongo import MongoClient
import time

logging.basicConfig(level=logging.DEBUG)
client = MongoClient('mongodb://localhost:27017')
db = client['yth_mvwchina']
db_questions = db['questions']

class GetPic:
    '''从MongoDB中去的需要下载的图片链接，使用requests.get方法获取图片文件保存在本地
    保存的路径按"https://exam.mvwchina.com//upload/2018/05/28/2f524adc4872401588tead8f6fb99fe38.png"中upload下面的目录结构
    '''
    def __init__(self):
        self.path_root = '/Users/chengfei/Documents/mvwchina'  #保存的本地根路径
        self.pic_type = 'jpg'  #另存的图片 格式1
        self.pic_type = 'png'  #另存的图片 格式2，看了一一些数据，应该主要是png格式的

    def get_pic_from_mongo(self):
        '''从mongodb中获取图片的url地址，为了保证不重复抓取将数据保存在dict中'''
        questions = db_questions.find({'havePictures':1}, no_cursor_timeout=True).batch_size(100)
        for question in questions:
            # 检查题目是否有图片
            pattern = re.compile(r'http[s]://(?:[a-zA-Z]|[0-9]|[$-_@.&+])+', re.I)
            imgs = re.findall(pattern, question['topic'])
            # 如果img List不为空获取图片
            if imgs:
                self.split_url(imgs)

            # 判读是否有答案，如果有答案从答案中获取图片，否则从子题的题干和答案中获取图片
            if question.get('choiceAnswers'):
                for answer in question['choiceAnswers']:
                    imgs = re.findall(pattern, answer['choiceanswer'])
                    # 如果img List不为空获取图片
                    if imgs:
                        self.split_url(imgs)
                # logging.info(imgs)
            else:  #有子题的图片获取，先获取子题，循环子题
                if question.get('chirlds'):
                    for chirld in question['chirlds']:
                        # 检查子题中的topic题目是否有图片
                        imgs = re.findall(pattern, chirld['topic'])
                        # 如果img List不为空获取图片
                        if imgs:
                            self.split_url(imgs)
                        if chirld.get('choiceAnswers'):
                            for answer in question['choiceAnswers']:
                                imgs = re.findall(pattern, answer['choiceanswer'])
                                # 如果img List不为空获取图片
                                if imgs:
                                    self.split_url(imgs)
        time.seelp(2)
        questions.close()


    def split_url(self, urls):
        '''将url list分解成url下载'''
        for url in urls:
            self.get_pic_from_webisite(url)


    def get_pic_from_webisite(self, url):
        '''从网站获取图片'''
        file_name = os.path.basename(url)
        dir_name = os.path.dirname(url)
        dir_name = dir_name.replace('https://exam.mvwchina.com/', '')
        if dir_name[0] != '/':
            dir_name = '/'+dir_name

        # 判断目录是否存在，不存在就创建
        save_path = self.path_root + dir_name
        self.mkdir( save_path)

        # 获取图片并保存
        response = get(url=url)
        pic = open(save_path + os.sep + file_name, 'wb')
        pic.write(response.content)
        pic.close()

        return

    def mkdir(self,path):
        '''创建目录，首先判断路径是否存在，如果不存在创建，存在直接返回'''
        isExists = os.path.exists(path)
        logging.info(path)
        if not isExists:
            os.makedirs(path)

        return

if __name__ == '__main__':
    getpic = GetPic()
    # getpic.get_pic_from_webisite('https://exam.mvwchina.com//upload/2018/05/02/5125c2d113494192a3a73a24f58bcd19.png')
    getpic.get_pic_from_mongo()