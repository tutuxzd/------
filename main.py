# -*- coding = uft-8 -*-
# @TIME : 2024/5/6 16:13
# @Author : Morisummer
# @File : main.py
# @Software : PyCharm
import cv2

# 读取图像
img = cv2.imread('apple.jpg')

# 中文文本内容
chinese_text = '你好，世界！'

# 文本位置和字体设置
font_path = '/Users/26757/Desktop/python/图片显示中文/font.ttf'  # 修改为你的字体文件路径
font_scale = 1.0
font_color = (0, 0, 255)
thickness = 2



# 在图像上添加中文文本
cv2.putText(img, chinese_text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, thickness, lineType=cv2.LINE_AA)

# 显示图像
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
