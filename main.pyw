import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import math
from PIL import Image, ImageTk
from tkinter import messagebox
from syw import *


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


def set_tag_side_4(event):
    global syw_tag_side_4_value
    widget = event.widget
    syw_tag_side_4_value = widget.get()
    syw_tag_2[4][0]['tag_name'] = syw_tag_side_4_value
    syw_tag_1[1].remove(syw_tag_side_4_value)


def set_tag_side_3(event):
    global syw_tag_side_3_value
    widget = event.widget
    syw_tag_side_3_value = widget.get()
    syw_tag_2[3][0]['tag_name'] = syw_tag_side_3_value
    syw_tag_1[1].remove(syw_tag_side_3_value)


def set_tag_side_2(event):
    global syw_tag_side_2_value
    widget = event.widget
    syw_tag_side_2_value = widget.get()
    syw_tag_2[2][0]['tag_name'] = syw_tag_side_2_value
    syw_tag_1[1].remove(syw_tag_side_2_value)


def set_tag_side_1(event):
    global syw_tag_side_1_value
    widget = event.widget
    syw_tag_side_1_value = widget.get()
    syw_tag_2[1][0]['tag_name'] = syw_tag_side_1_value
    syw_tag_1[1].remove(syw_tag_side_1_value)


def set_tag_main(event):
    global syw_tag_main_value
    widget = event.widget
    syw_tag_main_value = widget.get()
    syw_tag_2[0][0]['tag_name'] = syw_tag_main_value
    if syw_tag_main_value in syw_tag_1[1]:
        syw_tag_1[1].remove(syw_tag_main_value)


def search():
    # 获取圣遗物的词条
    # 检测筛选圣遗物的三个下拉框的值是否为空字符串
    if value_1.get() != '' and value_2.get() != '' and value_3.get() != '':
        shengyiwu = search_syw(value_1.get(), value_2.get(), value_3.get())
        global image

        image = ImageTk.PhotoImage(Image.open(shengyiwu[0][1]).resize((150, 150)))
        show_syw = tk.Label(window, text=shengyiwu[0][0], font=('黑体', 12), image=image, compound="bottom")
        show_syw.place(x=50, y=137)

        show_syw_effect.configure(text=shengyiwu[1])

        tk.Label(window, text='主词条', font=side_title_font).place(x=290, y=145)
        tk.Label(window, text='副词条', font=text_font).place(x=290, y=202)

        syw_tag_main = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_main['values'] = syw_tag_1[0][value_3.get()]
        syw_tag_main.place(x=290, y=175)
        syw_tag_main.bind('<<ComboboxSelected>>', set_tag_main)

        main_tag_value.place(x=400, y=178)

        syw_tag_side_1 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_side_1['values'] = syw_tag_1[1]
        syw_tag_side_1.bind('<<ComboboxSelected>>', set_tag_side_1)
        syw_tag_side_1.place(x=290, y=225)

        side_tag_1_value.place(x=400, y=228)

        syw_tag_side_2 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_side_2['values'] = syw_tag_1[1]
        syw_tag_side_2.bind('<<ComboboxSelected>>', set_tag_side_2)
        syw_tag_side_2.place(x=290, y=250)

        side_tag_2_value.place(x=400, y=253)

        syw_tag_side_3 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_side_3['values'] = syw_tag_1[1]
        syw_tag_side_3.bind('<<ComboboxSelected>>', set_tag_side_3)
        syw_tag_side_3.place(x=290, y=275)

        side_tag_3_value.place(x=400, y=278)

        syw_tag_side_4 = ttk.Combobox(window, textvariable=tk.StringVar(), state='readonly', width=12)
        syw_tag_side_4['values'] = syw_tag_1[1]
        syw_tag_side_4.bind('<<ComboboxSelected>>', set_tag_side_4)
        syw_tag_side_4.place(x=290, y=300)

        side_tag_4_value.place(x=400, y=303)

        huabu.create_line(257, 85, 257, 350, fill="#A0A0A0")
        huabu.create_line(0, 85, 515, 85, fill="#A0A0A0")

        evaluate_button = tk.Button(master=window, text='  评\t分  ', width=20, relief='groove')
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

title_font = ('微软雅黑', 25)
side_title_font = ('微软雅黑', 15)
text_font = ('微软雅黑', 10)

# separtor用来创建一个分割符
title_mian = tk.Label(window, text='原神圣遗物评分', font=title_font)
title_mian.pack(fill=tk.X)
ttk.Separator(window, orient=tk.HORIZONTAL).pack(fill=tk.X)

# 占位置的画布
huabu = tk.Canvas(window, height=350)
huabu.create_line(0, 349, 515, 349, fill="#A0A0A0")
huabu.pack(side='top', fill='x')

# 标题 评分结果
title_result = tk.Label(window, text='评分结果', font=side_title_font)
title_result.pack(fill=tk.X)
ttk.Separator(window, orient=tk.HORIZONTAL).pack(fill=tk.X)

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
tk.Label(window, text='请选择圣遗物星级', font=text_font).place(x=40, y=55)
tk.Label(window, text='请选择圣遗物', font=text_font).place(x=179, y=55)
tk.Label(window, text='请选择圣遗物部位', font=text_font).place(x=286, y=55)

# 按钮部分
search_button = tk.Button(master=window, text='确定', height=1, width=5, relief='groove', command=search)
search_button.place(x=420, y=82)

# 圣遗物效果
show_syw_effect = tk.Message(window, text='', font=('', 10), width=225)
show_syw_effect.place(x=10, y=310)

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
