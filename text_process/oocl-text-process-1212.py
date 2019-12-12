# -*- coding:utf-8 -*-
#!/usr/bin/python3

import os, re, shutil, time

pwd = os.getcwd()
zip_name = 'OOCL'
filename = 'transcription_with_file_extension_edit.txt'
audio_dir = os.path.join(pwd, 'Audio/')
pattern = re.compile('<.*/>')
data = []
new_data = []
now_time = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

text =  open(os.path.join(audio_dir, filename), "r", encoding = "utf-8")

if os.path.exists(now_time):
  pass
else:
  os.mkdir(now_time)
  trash = now_time

for line in text:
  context = line.split('\t')
  context[1] = re.sub(pattern, '', context[1]).strip()
  context[0].strip()
  if len(context[1]) == 0:
    shutil.move(os.path.join(audio_dir, context[0]), trash)
  else:
    data.append(context)
text.close()
shutil.move(os.path.join(audio_dir, filename), trash)

new_text = open(os.path.join(audio_dir, filename), 'w', encoding = 'utf-8')
for new_line in data:
  new_line[1] = new_line[1].__add__('\n')
  new_data.append('\t'.join(new_line))
new_text.write(''.join(new_data).rstrip())
new_text.close()

shutil.make_archive(zip_name, 'zip', 'Audio')