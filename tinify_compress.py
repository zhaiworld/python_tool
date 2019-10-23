import tinify
import os

'''
20 M 的图片能压缩到 2 M，压缩率达到惊人的 90%
'''
tinify.key = '此处填入你的key'
path = "C:\\Users\\yunpoyue\\Pictures\\cat"  # 图片存放的路径

for dirpath, dirs, files in os.walk(path):
    for file in files:
        imgpath = os.path.join(dirpath, file)
        print("compressing ..." + imgpath)
        tinify.from_file(imgpath).to_file(imgpath)
