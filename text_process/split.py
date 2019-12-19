# -*- coding:utf-8 -*-
import time

def open_diff():
    try:
        start = time.time()
        file = open('OOCL_zh-CN_transcriptions_30batches-201912191725-15.txt', 'r', encoding='utf-8')
        file.read()
        end = time.time()
        oepn_time = end - start
        file.close()
    except:
        print('打开失败')

    start = time.time()
    with open('OOCL_zh-CN_transcriptions_30batches-201912191725-15.txt', 'r', encoding='utf-8') as of:
        content = of.read()
        end = time.time()
        with_open_time = end - start

    return with_open_time - oepn_time

if __name__ == "__main__":
    sum = 0.0
    for i in range(1000):
        sum += float(open_diff())
    print('WITH OPEN 与 OPEN 两种方式打开此文件的时间差平均值为：',sum/1000 )