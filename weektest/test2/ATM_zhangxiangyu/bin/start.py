#coding:utf-8
import os,sys

res = os.path.dirname(os.path.dirname(__file__))
sys.path.append(res)

from core import src

if __name__ == '__main__':
    src.run()




