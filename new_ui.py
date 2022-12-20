import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import syw
import math
import numpy as np
import random


def get_font(size: int):
    font = ('微软雅黑', size)
    return font


def get_value():
    lvl_1 = random.randint(1, 6)
    lvl_2 = random.randint(1, 6)
    lvl_3 = random.randint(1, 6)
    lvl_4 = random.randint(1, 6)
    lvl_5 = random.randint(1, 6)
    lvl_6 = random.randint(1, 6)
    lvl_7 = random.randint(1, 6)
    score = random.randint(1, 50)
    value = ([lvl_1, lvl_2, lvl_3, lvl_4, lvl_5, lvl_6, lvl_7], score)
    return value


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


def draw(lvl):
    # 绘制雷达图
    a_p = set_polygon([125, 120], 80, 7)
    a = set_polygon([125, 120], 70, 7)
    b_p = set_polygon([125, 120], 60, 7)
    b = set_polygon([125, 120], 50, 7)
    c_p = set_polygon([125, 120], 40, 7)
    c = set_polygon([125, 120], 30, 7)
    d = set_polygon([125, 120], 20, 7)

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
    canvas.create_polygon(points_5, fill='#66c7e8', width=1)

    canvas.create_polygon(set_polygon([125, 120], 80, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 120], 60, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 120], 40, 7), fill='', outline='black', width=1)
    canvas.create_polygon(set_polygon([125, 120], 20, 7), fill='', outline='black', width=1)

    canvas.create_line(125, 120, a_p[0])
    canvas.create_line(125, 120, a_p[1])
    canvas.create_line(125, 120, a_p[2])
    canvas.create_line(125, 120, a_p[3])
    canvas.create_line(125, 120, a_p[4])
    canvas.create_line(125, 120, a_p[5])
    canvas.create_line(125, 120, a_p[6])

    canvas.pack(anchor='w', expand=True)


def get_text(value):
    score = value[1]
    pingjia = ''
    if score >= 0:
        pingjia = '平平无奇的'
        if score >= 30:
            pingjia = '中规中矩的'
            if score >= 50:
                pingjia = '百年一遇的'
    tuijian = ''
    score = str(int(score))+'分'
    print(value)
    if value[0][5] >= 3 or value[0][5] >= 4:
        tuijian = '推荐给主/副C使用'
    elif value[0][1] >= 3 or value[0][2] >= 2:
        tuijian = '推荐给辅助使用'
    elif value[0][5] >= 4 or value[0][7] >= 4 or value[0][4] >= 2:
        tuijian = '推荐给盾/奶使用'
    else:
        tuijian = '这件圣遗物貌似没有出众的地方'

    evaluate_result = '该圣遗物的分数是{}{}\n{}'.format(pingjia, score, tuijian)

    evaluate_text.configure(text=evaluate_result)


def evaluate():
    evaluate_title_sep.pack(fill=tk.X, before=evaluate_frame)
    evaluate_title.pack(fill=tk.X, before=evaluate_title_sep)
    evaluate_sep.pack(fill=tk.Y, side='left', before=evaluate_text_frame)

    value = get_value()
    get_text(value)
    draw(value[0])

    evaluate_text.pack(fill=tk.BOTH)


def click(event):
    widget = event.widget
    value = widget['text']
    if len(artifact_frame.winfo_children()) > 0:
        for i in artifact_frame.winfo_children():
            # print(i)
            i.destroy()
    images[5] = ImageTk.PhotoImage(Image.open(artifact[value][1]).resize((150, 150)))
    tk.Label(
        master=artifact_frame, text=artifact[value][0],
        image=images[5], compound='bottom', font=get_font(20)
             ).grid(column=0, row=2, columnspan=5, rowspan=6)
    # tk.Label(master=artifact_frame, text=('——' * 10)).grid(column=0, row=8, columnspan=5)
    # ttk.Separator(master=artifact_frame, orient=tk.HORIZONTAL)\
    #     .grid(column=0, row=1, columnspan=5, sticky='ew', pady=8)
    ttk.Separator(master=artifact_frame, orient=tk.HORIZONTAL).grid(column=0, row=8, columnspan=5, sticky='ew', pady=8)
    ttk.Separator(master=edit_frame, orient=tk.HORIZONTAL).grid(column=0, row=7, columnspan=5, sticky='ew', pady=9)
    tk.Label(master=artifact_frame, text=artifact['套装效果'], wraplength=200).grid(column=0, row=9, columnspan=5)

    main_window_sep.pack(fill=tk.X, before=evaluate_frame)
    show_sep.pack(fill=tk.Y, side='left')
    edit_frame.pack(fill=tk.Y, side='left')

    main_tag_title.grid(column=0, row=0, sticky='w', padx=5)
    main_tag_cmb.set('')
    main_tag_cmb.configure(values=syw.圣遗物词条[0][value])
    main_tag_cmb.grid(column=0, row=1, columnspan=2, padx=30)
    main_tag_entry.grid(column=3, row=1, padx=25)
    side_tag_title.grid(column=0, row=2, sticky='w', padx=10)
    side_tag_cmb_1.grid(column=0, row=3, columnspan=2, padx=20, pady=2)
    side_tag_cmb_2.grid(column=0, row=4, columnspan=2, padx=20, pady=2)
    side_tag_cmb_3.grid(column=0, row=5, columnspan=2, padx=20, pady=2)
    side_tag_cmb_4.grid(column=0, row=6, columnspan=2, padx=20, pady=2)
    side_tag_entry_1.grid(column=3, row=3, pady=2)
    side_tag_entry_2.grid(column=3, row=4, pady=2)
    side_tag_entry_3.grid(column=3, row=5, pady=2)
    side_tag_entry_4.grid(column=3, row=6, pady=2)
    evaluate_button.grid(column=0, row=8, padx=70, pady=12, columnspan=10, sticky='w')


def search(event):
    global artifact
    widget = event.widget
    value = widget.get()

    for i in syw.圣遗物:
        if i['name'] == value:
            artifact = i
            break

    keys = list(artifact.keys())
    num = len(keys)

    if len(choice_artifact_frame.winfo_children()) > 2:
        for i in choice_artifact_frame.winfo_children()[-5:]:
            # print(i)
            i.destroy()
    if len(edit_frame.winfo_children()) > 0:
        for i in edit_frame.winfo_children():
            i.grid_forget()
    if len(artifact_frame.winfo_children()) > 0:
        for i in artifact_frame.winfo_children():
            # print(i)
            i.destroy()
    choice_artifact_sep.pack(fill=tk.Y, side='left', padx=5)

    for i in range(0, num-2):
        images[i] = ImageTk.PhotoImage(Image.open(artifact[keys[i+1]][1]).resize((40, 40)))

        artifact_button = tk.Button(
            master=choice_artifact_frame, text=keys[i+1],
            font=get_font(10), compound='top', image=images[i]
        )
        artifact_button.bind('<Button-1>', click)
        artifact_button.pack(padx=5, pady=5, side='left')

    # tk.Label(master=artifact_frame, text=('——'*10)).grid(column=0, row=1, columnspan=5)


def init():
    global artifact_names
    for i in syw.圣遗物:
        artifact_names.append(i['name'])


artifact = {}
artifact_names = []
img_1 = ImageTk.PhotoImage
img_2 = ImageTk.PhotoImage
img_3 = ImageTk.PhotoImage
img_4 = ImageTk.PhotoImage
img_5 = ImageTk.PhotoImage
img_main = ImageTk.PhotoImage
# image = ImageTk.PhotoImage(Image.open(shengyiwu[0][1]).resize((150, 150)))
images = [img_1, img_2, img_3, img_4, img_5, img_main]

init()

main_window = tk.Tk()

artifact_name = tk.StringVar()

main_window.title('原神圣遗物评分')
main_window.iconbitmap('PingCe.ico')
scr_height = main_window.winfo_screenheight()
scr_width = main_window.winfo_screenwidth()
window_height = int(scr_height*0.75)
window_width = int(scr_width*0.35)
x = int((scr_width - window_width)*0.5)
y = int((scr_height - window_height)*0.5)
main_window.geometry('{}x{}+{}+{}'.format(str(window_width), str(window_height), str(x), str(y)))
# main_window.resizable(False, False)

choice_artifact_frame = tk.Frame(master=main_window)
show_frame = tk.Frame(master=main_window)
evaluate_frame = tk.Frame(master=main_window)

artifact_frame = tk.Frame(master=show_frame)
edit_frame = tk.Frame(master=show_frame)
main_tag_title = tk.Label(master=edit_frame, text='主词条', font=get_font(15))
main_tag_cmb = ttk.Combobox(master=edit_frame, values=[], width=13)
main_tag_entry = ttk.Entry(master=edit_frame, width=10)

side_tag_title = tk.Label(master=edit_frame, text='副词条', font=get_font(12))
side_tag_cmb_1 = ttk.Combobox(master=edit_frame, values=syw.圣遗物词条[1], width=13)
side_tag_cmb_2 = ttk.Combobox(master=edit_frame, values=syw.圣遗物词条[1], width=13)
side_tag_cmb_3 = ttk.Combobox(master=edit_frame, values=syw.圣遗物词条[1], width=13)
side_tag_cmb_4 = ttk.Combobox(master=edit_frame, values=syw.圣遗物词条[1], width=13)
side_tag_entry_1 = ttk.Entry(master=edit_frame, width=10)
side_tag_entry_2 = ttk.Entry(master=edit_frame, width=10)
side_tag_entry_3 = ttk.Entry(master=edit_frame, width=10)
side_tag_entry_4 = ttk.Entry(master=edit_frame, width=10)
evaluate_button = tk.Button(master=edit_frame, width=20, text='评\t分', command=evaluate)

evaluate_img_frame = tk.Frame(master=evaluate_frame)
# 设置画布
canvas = tk.Canvas(evaluate_img_frame, width=260, height=300)

evaluate_text_frame = tk.Frame(master=evaluate_frame)
evaluate_text = tk.Label(master=evaluate_text_frame, text='', wraplength=200)

main_title = tk.Label(master=main_window, text='圣遗物评分', font=get_font(25))
main_title.pack(fill=tk.X)

ttk.Separator(master=main_window, orient=tk.HORIZONTAL).pack(fill=tk.X)
choice_artifact_frame.pack(fill=tk.X)

search_artifact_cmb = ttk.Combobox(master=choice_artifact_frame, textvariable=artifact_name, values=artifact_names)
search_artifact_cmb.bind('<<ComboboxSelected>>', search)
search_artifact_cmb.pack(padx=5, pady=5, side='left')

ttk.Separator(master=main_window, orient=tk.HORIZONTAL).pack(fill=tk.X)
show_sep = ttk.Separator(master=show_frame, orient=tk.VERTICAL)
choice_artifact_sep = ttk.Separator(master=choice_artifact_frame, orient=tk.VERTICAL)
main_window_sep = ttk.Separator(master=main_window, orient=tk.HORIZONTAL)
evaluate_sep = ttk.Separator(master=evaluate_frame, orient=tk.VERTICAL)

show_frame.pack(fill=tk.X)
artifact_frame.pack(fill=tk.Y, side='left')

evaluate_title = tk.Label(master=main_window, text='评分结果', font=get_font(15))
evaluate_title_sep = ttk.Separator(master=main_window, orient=tk.HORIZONTAL)

evaluate_frame.pack(fill=tk.X)
evaluate_img_frame.pack(fill=tk.Y, side='left')
# 绘制7边形
canvas.create_text(125, 25, text='元素充能效率')
canvas.create_text(210, 65, text='元素精通')
canvas.create_text(227, 129, text='攻击力')
canvas.create_text(168, 204, text='伤害加成')
canvas.create_text(86, 206, text='爆率/爆伤')
canvas.create_text(30, 144, text='防御力')
canvas.create_text(48, 64, text='生命值')

evaluate_text_frame.pack(fill=tk.Y, side='left')

main_window.mainloop()
