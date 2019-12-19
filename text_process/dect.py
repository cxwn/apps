# -*- coding:utf-8 -*-
import chardet, os

path = os.getcwd()
res_set = set()

for file in os.listdir(path):
    with open(os.path.join(path, file), 'r', encoding='utf-8') as of:
        for line in of.readlines():
            res_set.add(chardet.detect(bytes(str(line),'utf-8'))['encoding'])

print(res_set)