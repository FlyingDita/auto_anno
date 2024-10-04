import tkinter as tk
import threading
import time
import sys
import cv2
from tkinter import filedialog


# 全局变量
drawing = False  # 鼠标按下标志
ix, iy = -1, -1  # 起始坐标
rectangles = []  # 存储矩形坐标
origin_folder_paths = []
output_folder_paths = []
color = [0,255,0]
class_id = 0


# 获取鼠标标注结果
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rectangles, color


    # print(color)

    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:  # 鼠标移动
        if drawing:
            img_copy = img.copy()  # 复制图像
            cv2.rectangle(img_copy, (ix, iy), (x, y), color, 1)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键抬起
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), color, 1)
        rectangles.append((ix, iy, x, y))  # 保存矩形坐标


def select_folder(folder_path):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 弹出文件夹选择对话框

    print(folder_path)
    return folder_path


def function1():
    global origin_folder_paths
    print("Function 1 is called")
    origin_folder_paths = select_folder(origin_folder_paths)
    # print(origin_folder_paths)

def function2():
    global output_folder_paths
    print("Function 2 is called")
    output_folder_paths = select_folder(output_folder_paths)

def function3():
    try:
        print("读取图片")
        while
        True:
            







            print("Thread working...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Thread interrupted!")
    finally:
        print("Exiting thread...")

def function4():
    print("选择 class_id")

def run_function3():
    thread = threading.Thread(target=function3, daemon=True)
    thread.start()

def run_function4():
    thread = threading.Thread(target=function4, daemon=True)
    thread.start()

def on_closing():
    print("Closing application...")
    root.destroy()
    sys.exit()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)

root.title("按钮功能示例")
# 设置界面大小
root.geometry('300x200')

# 创建按钮，并将其与相应的函数绑定
button1 = tk.Button(root, text="读取文件夹", command=function1)
button1.pack(pady=10)

button2 = tk.Button(root, text="选择输出标注文件路径", command=function2)
button2.pack(pady=10)

button3 = tk.Button(root, text="读取图片", command=run_function3)
button3.pack(pady=10)

button4 = tk.Button(root, text="Select class_id", command=run_function4)
button4.pack(pady=10)

try:
    root.mainloop()
except KeyboardInterrupt:
    on_closing()
