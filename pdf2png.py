#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: lzw5399 -*-
import os

import fitz


def pdf2image(pdf_path, img_path, zoom_x, zoom_y, rotation_angle):
    (_, file_fullname) = os.path.split(pdf_path)
    file_name = os.path.splitext(file_fullname)[0]

    # 打开PDF文件
    pdf = fitz.open(pdf_path)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        converted_image = os.path.join(img_path, file_name + '_' + str(pg) + ".png")
        pm.writePNG(converted_image)
        print(converted_image, '转换成功')
    pdf.close()


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.pdf':
            list_name.append(file_path)


if __name__ == '__main__':
    # 获取当前目录下所有的pdf
    pdfs = []
    current_dir = os.getcwd()
    listdir(current_dir, pdfs)

    # 创建images文件夹
    images_path = os.path.join(current_dir, 'images')
    if not os.path.exists(images_path):
        os.makedirs(images_path)

    # 遍历pdf转成png
    for pdfpath in pdfs:
        pdf2image(pdfpath, os.path.join(os.getcwd(), 'images'), 5, 5, 0)
