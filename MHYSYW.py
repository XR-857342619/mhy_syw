import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import math
from PIL import Image, ImageTk
from tkinter import messagebox
from syw import *


# 正文在400行左右
def set_title(master, text: str, size, cod: list = None, mod='A'):
    if mod == 'A':
        # 玄学设置字体大小
        font_size = int((int(width) / len(text)) / size)
        # 放置标签
        title = tk.Label(master, text=text, font=('微软雅黑', font_size))
        # 这地方可以不用这么麻烦，但是用了place方法的标签没法搞下划线
        title.pack(fill='x')
    if mod == 'M':
        title = tk.Label(master, text=text, font=('微软雅黑', size))
        title.place(x=cod[0], y=cod[1])


def search_syw(syw_lvl: str, syw_name: str, syw_widget: str):
    # 遍历列表
    shengyiwu = []
    i = 0
    if syw_lvl == '四星圣遗物':
        while i <= len(四星圣遗物)-1:
            if 四星圣遗物[i]['name'] == syw_name:
                shengyiwu.append(四星圣遗物[i][syw_widget])
                shengyiwu.append(四星圣遗物[i]['套装效果'])
            i += 1
    if syw_lvl == '五星圣遗物':
        while i <= len(五星圣遗物)-1:
            if 五星圣遗物[i]['name'] == syw_name:
                shengyiwu.append(五星圣遗物[i][syw_widget])
                """我也不知道为什么这顺序滞后了14"""
                shengyiwu.append(四星圣遗物[i+14]['套装效果'])
            i += 1
    # 返回一个列表 ： 圣遗物名字, 圣遗物套装效果
    return shengyiwu


def change_value(event):
    # 改变下拉框的选项，实现下拉框联动
    widget = event.widget
    value = widget.get()
    if value == '四星圣遗物':
        # 设置下拉框的默认值
        value_2.set('')
        # 设置下拉框的选项
        combobox_2.configure(values=combobox_values_2)
    elif value == '五星圣遗物':
        value_2.set('')
        combobox_2.configure(values=combobox_values_3)
    elif value != '' and value != '四星圣遗物' and value != '五星圣遗物':
        if value == '祭水之人' or value == '祭火之人' or value == '祭冰之人' or value == '祭雷之人':
            # 这几个都是只有理之冠的圣遗物
            combobox_3.set('')
            combobox_3.configure(values=['理之冠'])
        else:
            combobox_3.configure(values=combobox_values_4)


def rotate(angle, cod_1, cod_2):
    # 计算点绕点旋转后的坐标
    value_x = cod_1[0]
    value_y = cod_1[1]
    point_x = cod_2[0]
    point_y = cod_2[1]
    angle = math.radians(angle)
    value_x = np.array(value_x)
    value_y = np.array(value_y)
    rotate_x = (value_x-point_x)*math.cos(angle) - (value_y-point_y)*math.sin(angle) + point_x
    rotate_y = (value_x-point_x)*math.sin(angle) + (value_y-point_y)*math.cos(angle) + point_y
    # 返回一对整数
    return int(rotate_x), int(rotate_y)


def set_polygon(cod: list, size: int, edge: int):
    # 计算正多边形的顶点坐标
    angle = int(360/edge)
    # 每次旋转的角度
    point = []
    # 保存点的坐标
    i = 0
    while i <= edge:
        point_1 = cod
        point_2 = [cod[0], cod[1]-size]
        n_angle = angle * i
        point_x, point_y = rotate(angle=n_angle, cod_1=point_2, cod_2=point_1)
        point_cod = (point_x, point_y)
        point.append(point_cod)
        i += 1
    return point


def evaluate_4(lvl):
    # 绘制雷达图
    a_p = set_polygon([125, 135], 80, 7)
    a = set_polygon([125, 135], 70, 7)
    b_p = set_polygon([125, 135], 60, 7)
    b = set_polygon([125, 135], 50, 7)
    c_p = set_polygon([125, 135], 40, 7)
    c = set_polygon([125, 135], 30, 7)
    d = set_polygon([125, 135], 20, 7)

    point_1_lvl = lvl[0]
    point_2_lvl = lvl[1]
    point_3_lvl = lvl[2]
    point_4_lvl = lvl[3]
    point_5_lvl = lvl[4]
    point_6_lvl = lvl[5]
    point_7_lvl = lvl[6]

    point_5 = [d, c, c_p, b, b_p, a, a_p]
    points_5 = [
        point_5[point_1_lvl][0],
        point_5[point_2_lvl][1],
        point_5[point_3_lvl][2],
        point_5[point_4_lvl][3],
        point_5[point_5_lvl][4],
        point_5[point_6_lvl][5],
        point_5[point_7_lvl][6]
    ]
    canvas.create_polygon(points_5, fill='#83cbac', width=1)

    canvas.create_polygon(set_polygon([125, 135], 80, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 135], 60, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 135], 40, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 135], 20, 7), fill='', outline='black', width=1)

    canvas.create_line(125, 135, a_p[0])
    canvas.create_line(125, 135, a_p[1])
    canvas.create_line(125, 135, a_p[2])
    canvas.create_line(125, 135, a_p[3])
    canvas.create_line(125, 135, a_p[4])
    canvas.create_line(125, 135, a_p[5])
    canvas.create_line(125, 135, a_p[6])

    canvas.pack(anchor='w', expand='yes')


# noinspection PyTypeChecker
def evaluate_3():
    # 正式评分
    fenshu = 0

    lvl_5_1 = 0
    lvl_5_2 = 0
    lvl_5_3 = 0
    lvl_5_4 = 0
    lvl_5_5 = 0
    lvl_5_6 = 0
    lvl_5_7 = 0

    num = 0
    while num <= len(syw_tag_2)-1:
        if syw_tag_2[num][0]['tag_name'] == '暴击率':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_5 += 0.5
                if syw_tag_2[num][1]['tag_value'] >= 5:
                    lvl_5_5 += 0.5
                    if syw_tag_2[num][1]['tag_value'] >= 15:
                        lvl_5_5 += 0.5
                        if syw_tag_2[num][1]['tag_value'] >= 20:
                            lvl_5_5 += 0.5
                            if syw_tag_2[num][1]['tag_value'] >= 25:
                                lvl_5_5 += 0.5
            fenshu += syw_tag_2[num][1]['tag_value']*2
        if syw_tag_2[num][0]['tag_name'] == '暴击伤害':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_5 += 0.5
                if syw_tag_2[num][1]['tag_value'] >= 5:
                    lvl_5_5 += 0.5
                    if syw_tag_2[num][1]['tag_value'] >= 15:
                        lvl_5_5 += 0.5
                        if syw_tag_2[num][1]['tag_value'] >= 20:
                            lvl_5_5 += 0.5
                            if syw_tag_2[num][1]['tag_value'] >= 25:
                                lvl_5_5 += 0.5
            fenshu += syw_tag_2[num][1]['tag_value']
        if syw_tag_2[num][0]['tag_name'] == '攻击力(数值)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_3 += 1
                if syw_tag_2[num][1]['tag_value'] >= 50:
                    lvl_5_3 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 100:
                        lvl_5_3 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 150:
                            lvl_5_3 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 175:
                                lvl_5_3 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.25)
        if syw_tag_2[num][0]['tag_name'] == '攻击力(百分比)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_3 += 1
                if syw_tag_2[num][1]['tag_value'] >= 10:
                    lvl_5_3 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 20:
                        lvl_5_3 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 30:
                            lvl_5_3 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 40:
                                lvl_5_3 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.25)
        if syw_tag_2[num][0]['tag_name'] == '防御力(数值)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_5 += 1
                if syw_tag_2[num][1]['tag_value'] >= 50:
                    lvl_5_5 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 100:
                        lvl_5_5 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 150:
                            lvl_5_5 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 175:
                                lvl_5_5 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.025)
        if syw_tag_2[num][0]['tag_name'] == '防御力(百分比)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_5 += 1
                if syw_tag_2[num][1]['tag_value'] >= 10:
                    lvl_5_5 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 20:
                        lvl_5_5 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 30:
                            lvl_5_5 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 40:
                                lvl_5_5 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '生命值(数值)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_7 += 1
                if syw_tag_2[num][1]['tag_value'] >= 75:
                    lvl_5_7 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 150:
                        lvl_5_7 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 225:
                            lvl_5_7 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 300:
                                lvl_5_7 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.005)
        if syw_tag_2[num][0]['tag_name'] == '生命值(百分比)':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_7 += 1
                if syw_tag_2[num][1]['tag_value'] >= 12:
                    lvl_5_7 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 24:
                        lvl_5_7 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 36:
                            lvl_5_7 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 48:
                                lvl_5_7 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.1)
        if syw_tag_2[num][0]['tag_name'] == '治疗量加成':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_4 += 1
                if syw_tag_2[num][1]['tag_value'] >= 12:
                    lvl_5_4 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 24:
                        lvl_5_4 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 36:
                            lvl_5_4 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 48:
                                lvl_5_4 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.125)
        if syw_tag_2[num][0]['tag_name'] == '元素精通':
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_2 += 1
                if syw_tag_2[num][1]['tag_value'] >= 50:
                    lvl_5_2 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 100:
                        lvl_5_2 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 150:
                            lvl_5_2 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 175:
                                lvl_5_2 += 1
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.0125)
        if syw_tag_2[num][0]['tag_name'] == '元素充能效率':
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.1)
            if syw_tag_2[num][1]['tag_value'] > 0:
                lvl_5_1 += 1
                if syw_tag_2[num][1]['tag_value'] >= 15:
                    lvl_5_1 += 1
                    if syw_tag_2[num][1]['tag_value'] >= 30:
                        lvl_5_1 += 1
                        if syw_tag_2[num][1]['tag_value'] >= 45:
                            lvl_5_1 += 1
                            if syw_tag_2[num][1]['tag_value'] >= 60:
                                lvl_5_1 += 1
                                if syw_tag_2[num][1]['tag_value'] >= 75:
                                    lvl_5_1 += 1
        if syw_tag_2[num][0]['tag_name'] == '水元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '火元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '风元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '雷元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '草元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '冰元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '岩元素伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        if syw_tag_2[num][0]['tag_name'] == '物理伤害加成':
            lvl_5_5 += 4
            fenshu += int(syw_tag_2[num][1]['tag_value']*0.2)
        num += 1

    if value_1.get() == '五星圣遗物':
        fenshu = fenshu*0.90
    elif value_1.get() == '四星圣遗物':
        fenshu = fenshu*0.80

    pingjia = ''
    if fenshu >= 0:
        pingjia = '平平无奇的'
        if fenshu >= 30:
            pingjia = '中规中矩的'
            if fenshu >= 50:
                pingjia = '百年一遇的'

    # noinspection PyUnusedLocal
    tuijian = ''
    fenshu = str(int(fenshu))+'分'
    if lvl_5_5 >= 3 or lvl_5_5 >= 4:
        tuijian = '推荐给主/副C使用'
    elif lvl_5_1 >= 3 or lvl_5_2 >= 2:
        tuijian = '推荐给辅助使用'
    elif lvl_5_5 >= 4 or lvl_5_7 >= 4 or lvl_5_4 >= 2:
        tuijian = '推荐给盾/奶使用'
    else:
        tuijian = '这件圣遗物貌似没有出众的地方'
    evaluate_result = '该圣遗物的分数是{}{}\n{}'.format(pingjia, fenshu, tuijian)

    evaluate_text.configure(text=evaluate_result)
    if lvl_5_1 > 6:
        lvl_5_1 = 6
    if lvl_5_2 > 6:
        lvl_5_2 = 6
    if lvl_5_3 > 6:
        lvl_5_3 = 6
    if lvl_5_4 > 6:
        lvl_5_4 = 6
    if lvl_5_5 > 6:
        lvl_5_5 = 6
    if lvl_5_6 > 6:
        lvl_5_6 = 6
    if lvl_5_7 > 6:
        lvl_5_7 = 6
    lvl = [lvl_5_1, lvl_5_2, lvl_5_3, lvl_5_4, int(lvl_5_5), lvl_5_6, lvl_5_7]

    evaluate_4(lvl)


# noinspection PyTypeChecker
def evaluate_2():
    # 检查圣遗物词条
    error = None
    # 查找百分数词条
    i = 0
    while i <= len(syw_tag_2)-1:
        # if syw_tag_2[i][0]['tag_name'] == '生命值(百分比)' or syw_tag_2[i][0]['tag_name'] == '攻击力(百分比)' or \
        #     syw_tag_2[i][0]['tag_name'] == '防御力(百分比)' or syw_tag_2[i][0]['tag_name'] == '元素充能效率' or \
        #     syw_tag_2[i][0]['tag_name'] == '暴击率' or syw_tag_2[i][0]['tag_name'] == '暴击伤害' or \
        #     syw_tag_2[i][0]['tag_name'] == '物理伤害加成' or syw_tag_2[i][0]['tag_name'] == '火元素伤害加成' or \
        #     syw_tag_2[i][0]['tag_name'] == '水元素伤害加成' or syw_tag_2[i][0]['tag_name'] == '草元素伤害加成' or \
        #     syw_tag_2[i][0]['tag_name'] == '冰元素伤害加成' or syw_tag_2[i][0]['tag_name'] == '雷元素伤害加成' or \
        #     syw_tag_2[i][0]['tag_name'] == '风元素伤害加成' or syw_tag_2[i][0]['tag_name'] == '岩元素伤害加成' or \
        #         syw_tag_2[i][0]['tag_name'] == '治疗加成':
        if syw_tag_2[i][0]['tag_name'] in [
            '生命值(百分比)', '攻击力(百分比)', '防御力(百分比)', '元素充能效率', '暴击率', '暴击伤害', '物理伤害加成',
            '火元素伤害加成', '水元素伤害加成', '草元素伤害加成', '冰元素伤害加成', '雷元素伤害加成', '风元素伤害加成',
            '岩元素伤害加成', '治疗加成'
        ]:
            baifenshu = False
            # 检测词条的值是否为百分数
            for num_1 in str(syw_tag_2[i][1]['tag_value']):
                if num_1 == '%':
                    baifenshu = True
            if baifenshu:
                # 百分数转整数
                tag_value = str(syw_tag_2[i][1]['tag_value']).strip('%')
                syw_tag_2[i][1]['tag_value'] = int(float(tag_value))
            else:
                error = '%'
        i += 1
    # 各词条的值转整数
    num_2 = 0
    while num_2 <= len(syw_tag_2)-1:
        tag_value = syw_tag_2[num_2][1]['tag_value']
        try:
            syw_tag_2[num_2][1]['tag_value'] = int(tag_value)
        except ValueError:
            error = 'nan'
        num_2 += 1
    # 圣遗物词条查重
    num_3 = 0
    num_5 = 0
    num_4 = 0
    while num_3 <= len(syw_tag_2)-1:
        while num_4 <= len(syw_tag_2)-1:
            if syw_tag_2[num_3][0]['tag_name'] == syw_tag_2[num_4][0]['tag_name']:
                num_5 += 1
                if num_5 >= 2:
                    error = 'repeat'
                    num_5 = 0
            num_4 += 1
        num_3 += 1
    # 报错
    if error == '%':
        messagebox.showwarning('警告', '请在对应的百分数词条中填写百分数')
    elif error == 'nan':
        messagebox.showwarning('警告', '请在词条中填写正整数')
    elif error == 'repeat':
        messagebox.showwarning('警告', '圣遗物词条重复')
    else:
        evaluate_3()


def evaluate_1():
    # 获取各词条的值
    global main_tag_value_2
    main_tag_value_2 = main_tag_value.get()
    syw_tag_2[0][1]['tag_value'] = main_tag_value_2

    global side_tag_1_value_2
    side_tag_1_value_2 = side_tag_1_value.get()
    syw_tag_2[1][1]['tag_value'] = side_tag_1_value_2

    global side_tag_2_value_2
    side_tag_2_value_2 = side_tag_2_value.get()
    syw_tag_2[2][1]['tag_value'] = side_tag_2_value_2

    global side_tag_3_value_2
    side_tag_3_value_2 = side_tag_3_value.get()
    syw_tag_2[3][1]['tag_value'] = side_tag_3_value_2

    global side_tag_4_value_2
    side_tag_4_value_2 = side_tag_4_value.get()
    syw_tag_2[4][1]['tag_value'] = side_tag_4_value_2
    # 检测各词条的值是否为空字符串
    if syw_tag_2[0][1]['tag_value'] != '' and syw_tag_2[1][1]['tag_value'] != '' and \
            syw_tag_2[2][1]['tag_value'] != '' and syw_tag_2[3][1]['tag_value'] != '' and\
            syw_tag_2[4][1]['tag_value'] != '':
        tiaojian = True
    else:
        tiaojian = False
    if tiaojian:
        evaluate_2()
    # 报错
    else:
        messagebox.showwarning('警告', '请填写圣遗物词条具体数值')


def set_tag_side_4(event):
    global syw_tag_side_4_value
    widget = event.widget
    syw_tag_side_4_value = widget.get()
    syw_tag_2[4][0]['tag_name'] = syw_tag_side_4_value


def set_tag_side_3(event):
    global syw_tag_side_3_value
    widget = event.widget
    syw_tag_side_3_value = widget.get()
    syw_tag_2[3][0]['tag_name'] = syw_tag_side_3_value

    syw_tag_side_4 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
    syw_tag_side_4['values'] = syw_tag_1[1]
    syw_tag_side_4.bind('<<ComboboxSelected>>', set_tag_side_4)
    syw_tag_side_4.place(x=290, y=300)

    side_tag_4_value.place(x=400, y=303)


def set_tag_side_2(event):
    global syw_tag_side_2_value
    widget = event.widget
    syw_tag_side_2_value = widget.get()
    syw_tag_2[2][0]['tag_name'] = syw_tag_side_2_value

    syw_tag_side_3 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
    syw_tag_side_3['values'] = syw_tag_1[1]
    syw_tag_side_3.bind('<<ComboboxSelected>>', set_tag_side_3)
    syw_tag_side_3.place(x=290, y=275)

    side_tag_3_value.place(x=400, y=278)


def set_tag_side_1(event):
    global syw_tag_side_1_value
    widget = event.widget
    syw_tag_side_1_value = widget.get()
    syw_tag_2[1][0]['tag_name'] = syw_tag_side_1_value

    syw_tag_side_2 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
    syw_tag_side_2['values'] = syw_tag_1[1]
    syw_tag_side_2.bind('<<ComboboxSelected>>', set_tag_side_2)
    syw_tag_side_2.place(x=290, y=250)

    side_tag_2_value.place(x=400, y=253)


def set_tag_main(event):
    global syw_tag_main_value
    widget = event.widget
    syw_tag_main_value = widget.get()
    syw_tag_2[0][0]['tag_name'] = syw_tag_main_value

    syw_tag_side_1 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
    syw_tag_side_1['values'] = syw_tag_1[1]
    syw_tag_side_1.bind('<<ComboboxSelected>>', set_tag_side_1)
    syw_tag_side_1.place(x=290, y=225)

    side_tag_1_value.place(x=400, y=228)


def search():
    # 获取圣遗物的词条
    # 检测筛选圣遗物的三个下拉框的值是否为空字符串
    if value_1.get() != '' and value_2.get() != '' and value_3.get() != '':
        shengyiwu = search_syw(value_1.get(), value_2.get(), value_3.get())
        global image

        image = ImageTk.PhotoImage(Image.open(shengyiwu[0][1]).resize((150, 150)))
        show_syw = tk.Label(window, text=shengyiwu[0][0], font=('黑体', 15), image=image, compound="bottom")
        show_syw.place(x=50, y=130)

        show_syw_effect.configure(text=shengyiwu[1])

        set_title(window, text='主词条', size=15, cod=[290, 145], mod='M')
        set_title(window, text='副词条', size=10, cod=[290, 202], mod='M')

        syw_tag_main = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_main['values'] = syw_tag_1[0][value_3.get()]
        syw_tag_main.place(x=290, y=175)
        syw_tag_main.bind('<<ComboboxSelected>>', set_tag_main)

        main_tag_value.place(x=400, y=178)

        huabu.create_line(257, 85, 257, 350, fill="#A0A0A0")
        huabu.create_line(0, 85, 515, 85, fill="#A0A0A0")

        evaluate_button = tk.Button(master=window, text='  评\t分  ', width=20, relief='groove', command=evaluate_1)
        evaluate_button.place(x=300, y=330)
    else:
        messagebox.showwarning('警告', '请选择圣遗物')


# 各种数据的初始化
syw_tag_1 = 圣遗物词条[:]
syw_tag_2 = [
    [{'tag_name': ''}, {'tag_value': 0}],
    [{'tag_name': ''}, {'tag_value': 0}],
    [{'tag_name': ''}, {'tag_value': 0}],
    [{'tag_name': ''}, {'tag_value': 0}],
    [{'tag_name': ''}, {'tag_value': 0}],
]

image = None
syw_tag_main_value = ''
syw_tag_side_1_value = ''
syw_tag_side_2_value = ''
syw_tag_side_3_value = ''
syw_tag_side_4_value = ''
main_tag_value_2 = 0
side_tag_1_value_2 = 0
side_tag_2_value_2 = 0
side_tag_3_value_2 = 0
side_tag_4_value_2 = 0

combobox_values_list_1 = []
combobox_values_list_2 = []

num = 0
while num <= len(四星圣遗物)-1:
    combobox_values_list_1.append(四星圣遗物[num]['name'])
    num += 1
num = 0
while num <= len(五星圣遗物)-1:
    combobox_values_list_2.append(五星圣遗物[num]['name'])
    num += 1

combobox_values_1 = ('', '四星圣遗物', '五星圣遗物')
combobox_values_2 = tuple(combobox_values_list_1)
combobox_values_3 = tuple(combobox_values_list_2)
combobox_values_4 = ('生之花', '死之羽', '时之沙', '空之杯', '理之冠')

# UI界面
window = tk.Tk()
window.title('原神圣遗物评分')
window.iconbitmap('PingCe.ico')
height = str(int(window.winfo_screenheight()*0.75))
width = str(int(window.winfo_screenwidth()*0.35))
window.geometry('{}x{}'.format(width, height))
window.resizable(False, False)

# separtor用来创建一个分割符
ttk.Separator(set_title(window, '原神圣遗物评分', 3.5), orient=tk.HORIZONTAL).pack(fill=tk.X)

# 占位置的画布
huabu = tk.Canvas(window, height=350)
huabu.create_line(0, 349, 515, 349, fill="#A0A0A0")
huabu.pack(side='top', fill='x')

# 标题 评分结果
ttk.Separator(set_title(window, '评分结果', 8), orient=tk.HORIZONTAL).pack(fill=tk.X)

# 多行文本 评分结果
evaluate_text = tk.Message(window, text='', font=('', 10), width=243)
evaluate_text.place(x=275, y=475)

# 下拉框
# 设置下拉框的初始值
value_1 = tk.StringVar()
value_1.set(combobox_values_1[0])
combobox_1 = ttk.Combobox(window, textvariable=value_1, state='readonly', width=16)
# 设置下拉框的选项
combobox_1['values'] = combobox_values_1
combobox_1.current(0)
# 绑定函数
combobox_1.bind('<<ComboboxSelected>>', change_value)
# 设置位置
combobox_1.place(x=40, y=85)

value_2 = tk.StringVar()
value_2.set('')
combobox_2 = ttk.Combobox(window, textvariable=value_2, state='readonly', width=12)
combobox_2.bind('<<ComboboxSelected>>', change_value)
combobox_2.place(x=179, y=85)

value_3 = tk.StringVar()
value_3.set('')
combobox_3 = ttk.Combobox(window, textvariable=value_3, state='readonly', width=15)
combobox_3.bind('<<ComboboxSelected>>', change_value)
combobox_3.place(x=289, y=85)

# 标题部分
set_title(window, '请选择圣遗物星级', 12, cod=[40, 55], mod='M')
set_title(window, '请选择圣遗物', 12, cod=[179, 55], mod='M')
set_title(window, '请选择圣遗物部位', 12, cod=[286, 55], mod='M')

# 按钮部分
search_button = tk.Button(master=window, text='确定', height=1, width=5, relief='groove', command=search)
search_button.place(x=420, y=82)

# 圣遗物效果
show_syw_effect = tk.Message(window, text='', font=('', 10), width=225)
show_syw_effect.place(x=10, y=305)

# 圣遗物tag的value
main_tag_value = tk.Entry(window, font=('', 10), width=10)
side_tag_1_value = tk.Entry(window, font=('', 10), width=10)
side_tag_2_value = tk.Entry(window, font=('', 10), width=10)
side_tag_3_value = tk.Entry(window, font=('', 10), width=10)
side_tag_4_value = tk.Entry(window, font=('', 10), width=10)

# 设置画布
canvas = tk.Canvas(window, width=260, height=1000)
# 绘制7边形
canvas.create_text(125, 40, text='元素充能效率')
canvas.create_text(198, 75, text='元素精通')
canvas.create_text(217, 154, text='攻击力')
canvas.create_text(168, 219, text='伤害加成')
canvas.create_text(86, 221, text='爆率/爆伤')
canvas.create_text(33, 159, text='防御力')
canvas.create_text(48, 79, text='生命值')
# 绘制分割线

window.mainloop()
