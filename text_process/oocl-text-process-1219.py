# -*- coding:utf-8 -*-
import os, re, shutil, time, chardet

path = r'C:\Users\v-ruidu\Downloads\work\20191219\OOCL_zh-CN_transcriptions_30batches_random'
pattern = re.compile('<\\w*/>|\[(.*?)\]')
res = time.strftime("OOCL_zh-CN_transcriptions_30batches-%Y%m%d%H%M",time.localtime(time.time()))
context = ''
count = 0

for i in range(1,31):
    count = count + 1
    with open(os.path.join(path, 'OOCL_zh-CN_transcriptions_30batches_{}.txt'.format(str(i))), 'r', encoding='utf-8') as of:
        for line in of.readlines():
            row = re.sub(pattern, '', str(line))
            content = bytes(row, 'utf-8')
            if len(content) != 0:
                context += content.decode('utf-8').lstrip()
                if count == 1:
                    with open(res + '-' + str(count) + '.txt', 'w', encoding='utf-8') as rf:
                        rf.write(context)
                elif count % 5 == 0:
                    with open(res + '-' + str(count) + '.txt', 'w', encoding='utf-8') as rf:
                        rf.write(context)
                else:
                    pass
            else:
                pass
