# QA
直播答题辅助工具

# 原理说明
* 首先通过同屏软件或虚拟机来使直播界面同步出现在PC端的屏幕上。
* 通过Python的PIL库来截取屏幕上题目的题目，保存成图片。
* 通过pytesseract库从图片中识别题目的文字信息。
* 百度搜索题目供答题时参考。

# 使用说明
* 设置setting.json文件中的内容，其中x1、y1、x2、y2分别代表要截取图片位置的左上角和右下角坐标
  scope为图片的放大系数，用于截取图片后将原始图片放大后再用于识别。通过测试，可以明显提高识别率，
  可在不明显影响识别时间的前提下，结合当前识别率和显示器分辨率情况酌情设置。
* 运行QA.py文件，当题目出来时按回车进行截图识别，识别完后会自动百度。
* 该工具只能提供参考，有些题百度了也没用。

# 环境配置
* python2.7
* QA.py用到的库可以用pip或easy_install安装
* 安装tesseract识别引擎（[下载地址](http://download.csdn.net/download/u010389578/10216791)），安装过程中记住额外选择简体中文的语言包。
* 将Python\Lib\site-packages\pytesseract\pytesseract.py中的tesseract_cmd的值改为tesseract识别引擎的安装位置。
如tesseract_cmd = 'D:/Tesseract-OCR/tesseract.exe'
