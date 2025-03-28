import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

img = cv2.imread('apple.jpg')
img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 图像从OpenCV格式转换成PIL格式
font = ImageFont.truetype('font.ttf', 20)  # 20为字体大小，根据需要调整
fillColor = (255, 255, 0)
position = (100, 120)  # 第一个数值是距左，第二个数值是距上
str = '在此输入想要在图片上显示的中文'
draw = ImageDraw.Draw(img_PIL)
draw.text(position, str, font=font, fill=fillColor)
img = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)  # 转换回OpenCV格式
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()