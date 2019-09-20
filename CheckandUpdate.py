import requests
import json
import os
import urllib.request
from urllib import parse


def get_file_list():
    url = "https://api.github.com/repos/babgozd/camporter96-custom/contents/grid"
    data = requests.get(url)
    tmp_info = json.loads(data.text)
    # steam_dir=PATH
    print("""
          
  ______    ______   __     __   ______   __    __   ______   __       
 /      \  /      \ |  \   |  \ /      \ |  \  |  \ /      \ |  \      
|  $$$$$$\|  $$$$$$\| $$   | $$|  $$$$$$\| $$\ | $$|  $$$$$$\| $$      
| $$   \$$| $$   \$$| $$   | $$| $$ __\$$| $$$\| $$| $$___\$$| $$      
| $$      | $$       \$$\ /  $$| $$|    \| $$$$\ $$ \$$    \ | $$      
| $$   __ | $$   __   \$$\  $$ | $$ \$$$$| $$\$$ $$ _\$$$$$$\| $$      
| $$__/  \| $$__/  \   \$$ $$  | $$__| $$| $$ \$$$$|  \__| $$| $$_____ 
 \$$    $$ \$$    $$    \$$$    \$$    $$| $$  \$$$ \$$    $$| $$     \\
  \$$$$$$   \$$$$$$      \$      \$$$$$$  \$$   \$$  \$$$$$$  \$$$$$$$$
          Camporter96\'s Custom Vertical Grids for New Steam Library""")
    steam_dir = input(
        "Enter your Steam dir(like: E:/Program Files (x86)/Steam/userdata/****** ):") + '/config/grid/'
    if os.path.exists(steam_dir):
        current_file = os.listdir(steam_dir)
    else:
        os.mkdir(steam_dir)
        current_file = os.listdir(steam_dir)
    f_current = open('oldfilenames.txt', mode='w', encoding='utf-8')
    for i in range(len(current_file)):
        f_current.write(str(current_file[i])+'\n')
    f_current.close()
    f_github = open('newfilenames.txt', mode='w', encoding='utf-8')
    for i in range(len(tmp_info)):
        f_github.write(tmp_info[i]['name'] + '\n')
    f_github.close()
    return steam_dir


def pic_download():
    steam_dir = get_file_list()
    str1 = []
    str2 = []
    str_dump = []
    fa = open('newfilenames.txt', 'r')
    fb = open('oldfilenames.txt', 'r')
    str1 = fa.read().splitlines()
    str2 = fb.read().splitlines()
    fa.close()
    fb.close()
    os.remove('newfilenames.txt')
    os.remove('oldfilenames.txt')
    for i in str1:
        if i in str2:
            str_dump.append(i)
    for i in str_dump:
        if i in str1:
            str1.remove(i)
    if len(str1) != 0:
        for i in list(str1):
            f_newpic = open(steam_dir+i, mode='wb')
            newi = parse.quote(i).replace("\+", "%20")
            picurl = "https://raw.githubusercontent.com/babgozd/camporter96-custom/master/grid/"+newi
            newpic = urllib.request.urlopen(picurl)
            f_newpic.write(newpic.read())
            f_newpic.flush()
            f_newpic.close()
        print("[INFO]Download/Update is complete.\n[INFO]If have any questions,please report issues on github.")
    else:
        print("[INFO]Your files seem to be up to date.\n[INFO]If have any questions,please report issues on github.")


if __name__ == "__main__":
    pic_download()
    print("Github Page: https://github.com/babgozd/camporter96-custom")
    print("Repository(Artworks) Author: babgozd(https://github.com/babgozd)")
    print("Script Author: ithg (https://github.com/ithg)")
    os._exit(0)
