import requests
import json
import os
import urllib.request
from urllib import parse

url = "https://api.github.com/repos/babgozd/camporter96-custom/contents/grid"

data = requests.get(url)
tmp_info = json.loads(data.text)
#steam_dir=PATH
steam_dir=input("enter your steam dir(like: E:/Program Files (x86)/Steam/userdata/****** ):")
current_file=os.listdir(steam_dir+r'\config\grid')
f_current = open('oldfilenames.txt', mode='w', encoding='utf-8')
for i in range(len(current_file)):
    f_current.write(str(current_file[i])+'\n')
f_current.write('README.md\n')
f_current.close()
f_github = open('newfilenames.txt', mode='w', encoding='utf-8')
for i in range(len(tmp_info)):
    f_github.write(tmp_info[i]['name'] + '\n')
f_github.close()

str1 = []
str2 = []
str_dump = []
fa = open('oldfilenames.txt', 'r')
fb = open('newfilenames.txt', 'r')
str1 = fa.read().splitlines()
str2 = fb.read().splitlines()
for i in str1:
    if i in str2:
        str_dump.append(i)
str_all = set(str1 + str2)
for i in str_dump:
    if i in str_all:
        str_all.remove(i)
for i in list(str_all):
    f_newpic = open(steam_dir+'\\config\\grid\\'+i,mode='wb')
    newi =parse.quote(i).replace("\+", "%20")
    newpic = urllib.request.urlopen('https://raw.githubusercontent.com/babgozd/camporter96-custom/master/grid/'+newi)
    f_newpic.write(newpic.read())
    f_newpic.flush()
    f_newpic.close()
fa.close()
fb.close()