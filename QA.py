# -*- coding: utf-8 -*-
import time
from PIL import Image, ImageGrab
import pytesseract
import webbrowser
import json
import os, sys
import subprocess

global x1, y1, x2, y2, scope

def take_screenshot(filename):
    print("PrtSc")
    # 获取屏幕截图
    im = ImageGrab.grab((x1, y1, x2, y2))
    w = x2 - x1
    h = y2 - y1
    # 根据设置放大截取的图片，以提高多笔画字的识别率
    im = im.resize((int(scope*w), int(scope*h)), Image.ANTIALIAS)
    im.save(filename, quality = 95)

def get_settings():
    # 读取设置文件
    settings_file = 'settings.json'
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as file:
            print 'Load settings successful'
            return json.load(file)
    else:
        print 'Can\'t find setting.json'
        sys.exit()


# 读取设置
settings = get_settings()
x1 = settings['x1']
y1 = settings['y1']
x2 = settings['x2']
y2 = settings['y2']
scope = settings['scope']

while True:
    s = raw_input("Enter to continue")
    start = time.time()
    take_screenshot('screenshot.jpg')
    # 从图片识别文字
    text = pytesseract.image_to_string(Image.open('screenshot.jpg'), lang='chi_sim')
    text = ''.join(text.split())
    print text
    # 打开百度搜索
    url = 'http://www.baidu.com/s?wd=%s' % text
    webbrowser.open(url)
    end = time.time()
    out_text = 'It takes ' + str(end-start) + ' seconds'
    print out_text