# -*- coding: utf-8 -*-
import pickle
class icd10Code:
    """[summary]
    一个给icd10自动匹配编码
    
    """
    def __init__(self,data='icd10.plk',version="plus"):
        self.icd10=self.load(data)
        if version =="plus":
            self.icd10Dict=self.icd10['icd10DictPlus']
            self.dict2Icd10=self.icd10['word2icd10Plus']
        else:
            self.icd10Dict=self.icd10['icd10Dict']
            self.dict2Icd10=self.icd10['dict2Icd10']
            
        pass
    def load(self,data):
        with open(data,'rb') as f:
            icd10=pickle.load(f)
            return icd10
    def get_name(self,code=None):
        if code==None:
            return None
        try:
            return self.icd10Dict.get(str(code))
        except:
            return None
    def get_code(self,name=None):
        if name==None:
            return None
        try:
            return self.dict2Icd10.get(str(name))
        except:
            return None


if __name__ == '__main__':
    Icd10=icd10Code()
    print(Icd10.icd10.keys())
    word = input("输入疾病:")
    print(Icd10.get_code(word))

