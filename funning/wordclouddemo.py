import os

import wordcloud as wc
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 利用wordcloud生成词云分为三个步骤
# note: python3.9版wordcloud去链接 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载
if __name__ == '__main__':
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
    # 1. 获取文本txt
    filePath = os.path.join(os.path.join(PROJECT_DIR, "fileLibs"), "三国演义.txt")
    text = open(filePath, encoding='utf-8').read()
    # 2. 读取背景图片(须保证图片深度为8位，否则np.array处理时将报错，因此使用opencv来读取图片，安装命令pip install opencv-python)
    imgPath = os.path.join(os.path.join(PROJECT_DIR, "picLibs"), "guangong.jpg")
    img = cv2.imread(imgPath)
    background_img = np.array(img)
    # 3. 构造词云对象：中文文本时需要设置font_path，否则显示图片为方块
    w = wc.WordCloud(font_path='C:\Windows\Fonts\simfang.ttf',
                     mask=background_img,
                     background_color='white')
    # 4. 生成词云
    w.generate(text)
    # 5. 存储图片
    imgPath = os.path.join(os.path.join(PROJECT_DIR, "picLibs"), "wordcloud.png")
    w.to_file(imgPath)
    # 6. 图片展示
    plt.imshow(w, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    plt.show()