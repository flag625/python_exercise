#-*- coding: utf-8 -*-
#专利说明书摘要（英文）分词；去除标点、数字；词形还原；提取名词
#针对德温特专利记录的摘要，Excel格式，数据量在50左右
#输入单个Excel文件，输出新的Excel文件，包含标题和处理后的摘要单词两个项
import codecs #读取文件
import os
import pandas as pd  #读取Excel
#英语分词，词形还原，提取名词
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import wordnet

import json

class NlpPreProcess(object):
    """功能：
            preprocess_file(doc): 读取doc,去除标点和数字，词形还原，提取名词"""

    def __init__(self):
        super(NlpPreProcess,self).__init__()
        self.wml = WordNetLemmatizer() #词性还原
        #self.ps = PorterStemmer() #词干提取,选择使用
        self.allnum = 0

    def preprocess_file(self,filepath):
        """读取doc,去除标点和数字，词形还原，提取名词"""
        print('begin process %s' % filepath)
        df = pd.read_excel(filepath)
        df['cut_content'] = None
        #dict_w = {}
        save_path = u'E:/python/Abstract_spliting/new_excel/re.xlsx'
        #save_file = codecs.open(u'E:/python/Abstract_spliting/new_excel' + os.sep + 'split.json', 'w', 'utf-8')
        print('being process %s'%filepath)
        num = 0
        for dic in df.ix[:,5]:
            doc = str(dic).lower()
            for c in string.punctuation: #去标点
                doc = doc.replace(c,' ')
            for c in string.digits:#去数字
                doc = doc.replace(c,' ')
            doc = nltk.word_tokenize(doc) #分割成单词
            #只保留名词
            filter = nltk.pos_tag(doc)
            doc = [w for w, pos in filter if pos.startswith("NN")]
            cleanDoc = []
            for word in doc:
                if len(word)>=3 and wordnet.synsets(word):##只保留长度不小于3的单词，验证是否为英文单词（利用wordnet）
                    word = self.wml.lemmatize(word) #词形还原
                    cleanDoc.append(word)
            df['cut_content'][num] = ';'.join(cleanDoc) #保存为datafram
            #dict_w['content'] = ';'.join(cleanDoc)
            #json.dump(dict_w, save_file, ensure_ascii=False)
            #save_file.write('\n')
            num += 1
        df.to_excel(save_path)
        print('the num of valid docs is : %s' % num)
        print('---' * 20)

if __name__ == '__main__':
    filepath = u'E:\python\Abstract_spliting\data\综合电力+C类.xlsx'
    nlp_preprocess = NlpPreProcess()
    nlp_preprocess.preprocess_file(filepath)