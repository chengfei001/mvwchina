import logging
from json import loads
from pymongo import MongoClient

logging.basicConfig(level = logging.DEBUG)

client = MongoClient('mongodb://localhost:27017')
db = client['yth_mvwchina']

'''
讲keyword.json的数据保存的MongoDB
'''
if __name__ == '__main__':
    # 讲keyword数据单独获取保存
    keys = ('banks', 'keywords','keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'keyword6')

    # 读取keyword json文件
    with open('/Users/chengfei/Desktop/mvwchina_keyword.json') as file_keywords:
        str = file_keywords.read()
        dict_keywords = loads(str)

        # 通过keyword的大分类获取数据
        for key in keys:
            # 获取分类中子类的数据
            for dict_key in dict_keywords[key]:
                # 判断大分类中是否子类，如果有dict_key的内容为string，否则为dict
                if isinstance(dict_key,dict):
                    db[key].insert_many([dict_key])
                else:
                    db[key].insert_many(dict_keywords[key][dict_key])
                pass